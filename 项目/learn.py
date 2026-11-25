import re
products = [
    "电脑 价格: 5000元, 状态: 有货",
    "鼠标 价格: 50元, 状态: 缺货",
    "键盘 价格: 200元, 状态: 有货",
    "显示器 价格: 1500元, 状态: 有货"
]
reltq = [int(re.findall(r"\d+", r)[0]) for r in products if "有货" in r]
print(reltq)
