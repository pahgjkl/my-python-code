import requests
import re
url = "http://quotes.toscrape.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

}
print("正在请求网页...")
try:
    response = requests.get(url, headers=headers, timeout=5)
    if response.status_code == 200:
        print("成功")
        html_content = response.text
        pattern = r'<span class="text".*?>(.*?)</span>'
        quotes = re.findall(pattern, html_content, re.S)
        print(f"\n一共抓到了 {len(quotes)} 条名言:")

    else:
        print(f"失败, {response.status_code}")
except Exception as e:
    print(e)
try:
    response = requests.get(url, headers=headers, timeout=5)
    if response.status_code == 200:
        print("成功")
        html_content = response.text
        pattern = r'<small class="author".*?>(.*?)</small>'
        quotes1 = re.findall(pattern, html_content, re.S)
        print(f"\n一共抓到了 {len(quotes1)} 条名字:")
    else:
        print(f"失败, {response.status_code}")
except Exception as e:
    print(e)
for quotes1, quotes in zip(quotes1, quotes):
    print(f"{quotes1}:    {quotes}")
