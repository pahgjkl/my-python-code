import pandas as pd
my_records = [
    {"项目": "午饭", "金额": 30, "类型": "支出"},
    {"项目": "打车", "金额": 50, "类型": "支出"},
    {"项目": "工资", "金额": 10000, "类型": "收入"},
    {"项目": "晚饭", "金额": 40, "类型": "支出"},
    {"项目": "外快", "金额": 500, "类型": "收入"}
]
df = pd.DataFrame(my_records)
print("--- 1. 我的数据表格长这样 ---")
print(df)
print("\n")
print("--- 2. 计算总支出 ---")
expense_rows = df[df["类型"] == "支出"]
total_expense = expense_rows["金额"].sum()
print(F"总支出:{total_expense}")
print("\n")
print("--- 2. 计算总收入 ---")
income_rows = df[df["类型"] == "收入"]
total_income = income_rows["金额"].sum()
print(F"总收入:{total_income}")
print("\n")
print("\n--- 4. 打印出所有的支出明细 ---")
print(total_expense)
print(total_income)