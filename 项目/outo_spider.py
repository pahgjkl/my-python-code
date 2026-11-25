import requests
import re
import pandas as pd
import matplotlib.pyplot as plt
import time
all_quotes = []
for page in range(1, 4):
    print(f"正在爬取第 {page} 页...")
    url = f"http://quotes.toscrape.com/page/{page}/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            quotes = re.findall(r'<span class="text".*?>(.*?)</span>', response.text, re.S)
            outhors = re.findall(r'<small class="author".*?>(.*?)</small>', response.text, re.S)
            for q, a in zip(quotes, outhors):
                all_quotes.append({"名言": q.strip(), "作者": a.strip()})
            print(f"第{page}页解析成功")
    except Exception as e:
        print(e)
    time.sleep(1.5)
print(f"\n✅ 爬取完毕！一共抓到了 {len(all_quotes)} 条数据。")
df = pd.DataFrame(all_quotes)
print("\n--- 这是表格的前 5 行 ---")
print(df.head())
df.to_excel("名言大全.xlsx", index=False)
print("\n✅ 数据已保存为 名言大全.xlsx")
outhor_counts = df["作者"].value_counts()
print("\n---统计完毕, 正在生成图表---")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
outhor_counts.plot(kind='bar', color='orange', title="名言作者出场次数排行榜")
plt.ylabel("名言数量")
plt.xticks(rotation=45)
plt.show()