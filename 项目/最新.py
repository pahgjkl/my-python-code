import requests


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

        outer_list = cards[0].get("content", [])

        if outer_list and "content" in outer_list[0]:
            real_hot_list = outer_list[0]["content"]
        else:
            real_hot_list = outer_list

        news_text = ""
        for i, item in enumerate(real_hot_list[:3]):
            title = item.get("word", "未知热搜")
            # 获取 API 里的 url，如果没有，就用百度搜索的链接兜底
            url = item.get("url", f"https://www.baidu.com/s?wd={title}")

            # 【核心修改】使用 <a> 标签包裹标题，并加上样式（去下划线，变蓝）
            news_text += f'<div style="margin-bottom: 8px;">{i + 1}. <a href=" " target="_blank" style="color: #2980b9; text-decoration: none; font-weight: bold;">{title}</a ></div>'

        return news_text
    except Exception as e:
        return f"热搜获取失败：({e})"
hi = get_hot_news()
print(hi)