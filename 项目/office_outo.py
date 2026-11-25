import pandas as pd
data_a = {
    "学号": ["001", "002", "003", "004"],
    "姓名": [" 张三", "李四 ", "王五", "赵六"] # 注意张三和李四前后有空格
}
df_a = pd.DataFrame(data_a)
data_b = {
    "学号": ["003", "001", "004", "002"], # 顺序是乱的
    "高数成绩": [58, 95, 72, 45]          # 还有不及格的
}
df_b = pd.DataFrame(data_b)
df_merged = pd.merge(df_a, df_b, on="学号")
print(df_merged)
df_merged["姓名"] = df_merged["姓名"].str.strip()
df_merged = df_merged.sort_values(by="高数成绩", ascending=False)
print(df_merged)
df_merged.to_excel("排版前.xlsx", index=False)
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment

wb = load_workbook("排版前.xlsx")
ws = wb.active
for cell in ws[1]:
    cell.font = Font(bold=True)
    cell.alignment = Alignment(horizontal="center")
    cell.fill = PatternFill(start_color="00B0F0", end_color="00B0F0", fill_type='solid')
for row in ws.iter_rows(min_row=2):
    score_cell = row[2]
    if score_cell.value < 60:
        score_cell.font = Font(color="FF0000", bold=True)
ws.column_dimensions["A"].width = 15
ws.column_dimensions["B"].width = 15
ws.column_dimensions["C"].width = 15
wb.save("最终.xlsx")
