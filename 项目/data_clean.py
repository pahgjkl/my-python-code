import pandas as pd
import matplotlib.pyplot as plt
# # 1. 捏一个“脏”的工地材料进料单
# data = {
#     "单据号": [1, 2, 3, 3, 5],
#     "材料": ["水泥", "沙子", "钢筋", "钢筋", "砖块"],
#     "重量": [50, None, "100吨", "100吨", -20]
# }
#
# # 把字典变成 DataFrame 表格
# df = pd.DataFrame(data)
#
# print("--- 这是清洗前的脏数据 ---")
# print(df)
# print("\n--- 第一步：去重后 ---")
# df = df.drop_duplicates()
# print(df)
# print("\n--- 第二步：洗掉'吨'字后 ---")
# df['重量'] = df['重量'].astype(str).str.replace('吨', '')
# df['重量'] = df['重量'].replace('None', None)
# df['重量'] = pd.to_numeric(df['重量'], errors='coerce')
# print(df)
# print("\n--- 第三步：剔除负数异常值 ---")
# df = df.dropna()
# df = df[df['重量'] > 0]
# print(df)
# print("\n--- 最终检验 ---")
# print(f"这批材料的总重量是: {df['重量'].sum()} 吨")
# # 打印一下数据类型，看看是不是变成了 float64 或 int64
# print(f"当前重量的数据类型是: {df['重量'].dtype}")
# df.to_excel("洗干净的工地数据.xlsx", index=False)
# print("\n✅ 文件已成功保存到当前项目文件夹！")
data2 = {
    "材料": ["钢筋", "水泥", "钢筋", "砖块", "水泥", "钢筋"],
    "重量": [10, 20, 30, 5, 15, 40]
}
df2 = pd.DataFrame(data2)

print("\n--- 分组聚合：每种材料的总重量 ---")
# 按“材料”分组，算“重量”的总和
grouped = df2.groupby("材料")["重量"].sum()
print(grouped)
plt.rcParams['font.sans-serif'] = ['SimHei']
print("\n---正在生成柱状图---")
grouped.plot(kind='bar', color='skyblue')
plt.ylabel("重量  (吨)  ")
plt.show()