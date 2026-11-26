import smtplib
from email.mime.text import MIMEText
from email.header import Header
import requests

# ================= 1. 配置 =================
SMTP_SERVER = "smtp.qq.com"
SENDER_EMAIL = "3401731673@qq.com"
AUTH_CODE = "xfveuaowlgftciji"
RECIPIENTS = [
    {
        "email": "3401731673@qq.com",
        "name": "主人",
        "city": "Xiangtan",
        "greeting": "早上好呀，主人！",
    },
    {
        "email": "3401731673@qq.com",
        "name": "宝宝",
        "city": "Changsha",
        "greeting": "早安，宝宝，今天也是美好的一天！",
    }
]


# ================= 2. 获取天气与穿衣建议 (方向1) =================
def get_weather_and_clothing(city):
    try:
        url = f"https://wttr.in/{city}?format=j1&lang=zh"
        response = requests.get(url, timeout=15)
        data = response.json()
        current = data["current_condition"][0]
        temp = int(current["temp_C"])  # 转成整数方便判断

        try:
            desc = current["lang_zh"][0]["value"]
        except (KeyError, IndexError):
            desc = current["weatherDesc"][0]["value"]

        # 智能穿衣逻辑
        if temp < 10:
            clothes = "🥶 气温极低，记得穿羽绒服或厚棉服，千万别冻着！"
        elif 10 <= temp < 20:
            clothes = "🧥 天气微凉，建议穿外套或卫衣。"
        elif 20 <= temp < 28:
            clothes = "👕 温度适宜，穿长袖或短袖都可以。"
        else:
            clothes = "🥵 天气炎热，短袖短裤安排上，注意防晒多喝水！"

        return f"{desc}，当前温度 {temp}℃", clothes
    except Exception as e:
        return f"天气获取失败，请自行观察窗外。({e})", "穿衣建议获取失败。"


# ================= 3. 获取每日早报 (方向3) =================
def get_hot_news():
    try:
        api_url = "https://top.baidu.com/api/board?platform=wise&tab=realtime"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Referer": "https://top.baidu.com/"
        }

        response = requests.get(api_url, headers=headers, timeout=10)
        data = response.json()

        cards = data.get("data", {}).get("cards", [])
        if not cards:
            return "热搜接口暂时无法访问。"

        # 第一层：拿到外层列表
        outer_list = cards[0].get("content", [])

        # 第二层：如果外层列表有东西，且里面还有 content，就把真正的热搜列表挖出来！
        if outer_list and "content" in outer_list[0]:
            real_hot_list = outer_list[0]["content"]
        else:
            real_hot_list = outer_list  # 备用防错

        news_text = ""
        # 循环真正的热搜列表
        for i, item in enumerate(real_hot_list[:3]):
            # 现在 item 里面绝对有 word 了
            title = item.get("word", "未知热搜")
            news_text += f"{i + 1}. {title}<br>"

        return news_text

    except Exception as e:
        return f"热搜获取失败：({e})"


# ================= 4. 获取名言 =================
def get_quote():
    try:
        response = requests.get("https://v1.hitokoto.cn/?c=k", timeout=10)
        data = response.json()
        return f"“{data['hitokoto']}” —— {data.get('from', '佚名')}"
    except Exception:
        return "今天也要加油鸭！"


# ================= 5. 发送 HTML 精美邮件 (方向4) =================
def send_mail():
    quote = get_quote()
    hot_news = get_hot_news()

    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, 465, timeout=20)
        server.login(SENDER_EMAIL, AUTH_CODE)
    except Exception as e:
        print(f"[FAIL] 登录失败, {e}")
        return

    for r in RECIPIENTS:
        weather_text, clothing_tip = get_weather_and_clothing(r["city"])

        # 下雨预警判断
        rain_tip = ""
        if "雨" in weather_text:
            rain_tip = "<br><span style='color:red; font-weight:bold;'>⚠️ 管家提醒：今天有雨，记得带伞哦！</span>"

        # 【核心改变】组装 HTML 格式的邮件内容
        mail_content = f"""
        <div style="font-family: 'Microsoft YaHei', sans-serif; color: #333; line-height: 1.6; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
            <h2 style="color: #2c3e50;">{r['greeting']}</h2>

            <h3 style="color: #3498db; border-bottom: 2px solid #3498db; padding-bottom: 5px;">🌤️ 今日天气 ({r['city']})</h3>
            <p style="font-size: 16px;">{weather_text}{rain_tip}</p >

            <h3 style="color: #e67e22; border-bottom: 2px solid #e67e22; padding-bottom: 5px;">👔 智能穿衣</h3>
            <p style="font-size: 16px; background-color: #fff3e0; padding: 10px; border-radius: 5px;">{clothing_tip}</p >

            <h3 style="color: #c0392b; border-bottom: 2px solid #c0392b; padding-bottom: 5px;">🔥 今日热搜早报</h3>
            <p style="font-size: 15px;">{hot_news}</p >

            <h3 style="color: #27ae60; border-bottom: 2px solid #27ae60; padding-bottom: 5px;">📖 今日鸡汤</h3>
            <p style="font-size: 15px; font-style: italic; color: #555;">{quote}</p >

            <hr style="border: none; border-top: 1px dashed #ccc; margin: 20px 0;">
            <p style="font-size: 12px; color: #999; text-align: center;">此邮件由您的私人服务器自动发出，祝您度过美好的一天！</p >
        </div>
        """

        # 注意这里：把 'plain' 改成了 'html'
        message = MIMEText(mail_content, 'html', 'utf-8')
        message['From'] = SENDER_EMAIL
        message['To'] = r["email"]
        message['Subject'] = Header(f"☀️ {r['name']} 的专属早安日报已送达", 'utf-8')

        try:
            server.sendmail(SENDER_EMAIL, [r["email"]], message.as_string())
            print(f"[OK] 已发送给 {r['name']} <{r['email']}>")
        except Exception as e:
            print(f"[FAIL] 发送给 {r['name']} 失败: {e}")

    server.quit()


if __name__ == "__main__":
    send_mail()