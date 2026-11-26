import streamlit as st
import pandas as pd
import io
st.set_page_config(page_title="万能办公助手", page_icon="🛠️", layout="wide")
st.title("🛠️ 万能 Excel 自动化清洗工具")
st.write("上传任意 Excel 表格，在这里自由进行去重、填空、排序和筛选!")
uploaded_file = st.file_uploader("请选择你的 Excel 文件", type=["xlsx"])
st.write("最终解释权归刘磊所有")
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    col1, col2 = st.columns([1,2])
    with (col1):
        st.subheader("⚙️ 清洗选项")
        if st.checkbox("去除完全重复的行"):
            df = df.drop_duplicates()
            st.success("已去重")
        na_action = st.radio("处理空白格:", ["不处理", "删除有空白的行", "把空白填为0"])
        if na_action == "删除有空白的行":
                df = df.dropna()
                st.success("已删除空白行")
        elif na_action == "把空白填为0":
                df = df.fillna(0)
                st.success("已填充空值")
        st.markdown("---")
        st.subheader("排序与筛选")
        columns = df.columns.tolist()
        sort_col = st.selectbox("选择按哪一列排序：", ["不排序"] + columns)
        if sort_col != "不排序":
            sort_order = st.radio("排序方式：", ["降序 (从大到小)", "升序 (从小到大)"])
            assending = True if "升序" in sort_order else False
            df = df.sort_values(by=sort_col, ascending=assending)
        st.markdown("---")
        selected_cols = st.multiselect("选择你想要保留的列：", columns, default=columns)
        if selected_cols:
            df = df[selected_cols]
        if st.checkbox("清除所有文本的首尾空格"):
            for col in df.select_dtypes(include=['object']).columns:
                df[col] = df[col].astype(str).str.strip()
            st.success("已清除首尾空格")
    with (col2):
        st.subheader("✨ 实时处理结果")
        # 网页上实时展示处理后的表格
        st.dataframe(df, width="stretch")
        st.markdown("---")
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df.to_excel(writer, index=False)
        excel_output = output.getvalue()
        st.download_button(
            label="📥 下载处理好的 Excel",
            data=excel_output,
            file_name="清洗后的数据.xlsx",
            mime="application/vnd.openxmlformats.spreadsheetml.sheet",
            type="primary"

        )