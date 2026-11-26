import streamlit as st
import pandas as pd
import io  # 用于在内存里处理文件
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment

st.title("🏗️ 智能建造 - 自动化办公助手")
st.write("欢迎使用！请上传你的原始 Excel 表格，系统将自动进行数据清洗和合并.---最终解释权由刘磊所有")

uploaded_file = st.file_uploader("请选择你的 Excel 文件", type=["xlsx"])

if uploaded_file is not None:
    st.success("文件上传成功！正在处理...")

    # 1. 读取数据
    df = pd.read_excel(uploaded_file)

    st.subheader("📄 这是你的原始数据：")
    st.dataframe(df)

    try:
        # 2. 清洗数据 (加了 try 防止报错让网页崩溃)
        if "姓名" in df.columns:
            df["姓名"] = df["姓名"].str.strip()

        if "高数成绩" in df.columns:
            df = df.sort_values(by="高数成绩", ascending=False)

        st.subheader("✨ 经过 AI 清洗后的数据：")
        # 3. 将处理好的数据存到内存里，供用户下载
        # 因为网页不能直接把文件存到用户电脑上，必须提供下载按钮
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
        output.seek(0)
        wb = load_workbook(output)
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
        wb.save(output)
        # 注意这里，展示的是 df 而不是 ws
        st.dataframe(df)
        excel_data = output.getvalue()
        # 4. 在网页上生成一个下载按钮
        st.download_button(
            label="📥 点击下载处理好的 Excel",
            data=excel_data,
            file_name="清洗后的数据.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"数据清洗时发生错误：{e}")