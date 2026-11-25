# def my_devorator(func):
#     def wrapper():
#         print("-*3")
#         func()
#         print("-*3")
#     return wrapper
# @my_devorator
# def say_hello():
#     print("hello")
# say_hello()
# def star_wrapper(func):
#     def wrapper(*args, **kwargs):
#         print("**5")
#         func(*args, **kwargs)
#         print("**6")
#     return wrapper
# @star_wrapper
# def yui(name, age):
#     print(f"你好, 我是{name}, 今年{age}")
# yui("zhangyu", 22)


# import pandas as pd
# import os
# folder_path = r"D:\项目"
# all_data = []
# for file in os.listdir(folder_path):
#     if file.endswith(".xlsx"):
#         df = pd.read_excel(os.path.join(folder_path, file), dtype={"学号": str})
#         df = df.dropna()
#         all_data.append(df)
# final_df = pd.concat(all_data, ignore_index=True)
# final_df = final_df.drop_duplicates(subset=["学号"])
# final_df = final_df.sort_values(by="学号")
# final_df = final_df.reset_index(drop=True)
# final_df.to_excel("终极.xlsx", index=False)
# from openpyxl import load_workbook
# from openpyxl.styles import Font, PatternFill, Alignment
# wb = load_workbook("终极.xlsx")
# ws = wb.active
# for cell in ws[1]:
#     cell.font = Font(bold=True)
#     cell.alignment = Alignment(horizontal="center")
#     cell.fill = PatternFill(start_color="00B0F0", end_color="00B0F0", fill_type='solid')
# for row in ws.iter_rows(min_row=2):
#     score_cell = row[2]
#     if score_cell.value < 60:
#         score_cell.font = Font(color="FF0000", bold=True)
# ws.column_dimensions["A"].width = 15
# ws.column_dimensions["B"].width = 15
# ws.column_dimensions["C"].width = 15
# wb.save("终极.xlsx")
text = []
sentences = ["I love AI", "Python is great", "ML is fun"]
sentences_sp = [sentence.split() for sentence in sentences]
for sentence in range(len(sentences_sp)):
    for i in range(3):
        text.append(sentences_sp[sentence][i])
text_set = set(text)
print(text_set)