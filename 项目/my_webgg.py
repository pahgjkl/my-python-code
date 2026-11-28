import streamlit as st
import pandas as pd
import io
import numpy as np

# ================= 页面基础设置 =================
st.set_page_config(page_title="全能数据瑞士军刀", page_icon="🛠️", layout="wide")
st.title("🛠️ 全能 Excel 自动化清洗与处理平台")
st.caption("上传表格，左侧一键完成清洗、转换、计算与统计。")

# ================= 侧边栏：所有操作面板 =================
with st.sidebar:
    st.header("⚙️ 数据控制台")
    uploaded_file = st.file_uploader("请上传 Excel 或 CSV 文件", type=["xlsx", "csv"])

    # 如果上传了文件，才显示后续操作
    if uploaded_file is not None:
        # 1. 读取数据
        try:
            if uploaded_file.name.endswith('.csv'):
                # 尝试用 utf-8 读取，失败则尝试 gbk (国内常见编码)
                try:
                    df = pd.read_csv(uploaded_file, encoding='utf-8')
                except UnicodeDecodeError:
                    df = pd.read_csv(uploaded_file, encoding='gbk')
            else:
                df = pd.read_excel(uploaded_file)
            st.success("✅ 文件读取成功！")
        except Exception as e:
            st.error(f"❌ 读取失败: {e}")
            st.stop()  # 停止运行，防止后面代码报错

        # 展示所有列名供用户参考
        columns = df.columns.tolist()

        # 2. 数据概览 (仪表盘)
        st.markdown("---")
        st.subheader("📊 数据概览")
        c1, c2 = st.columns(2)
        c1.metric("总行数", len(df))
        c2.metric("总列数", len(df.columns))

        # 3. 基础清洗
        st.markdown("---")
        st.subheader("🧹 基础清洗")
        if st.checkbox("删除完全重复的行"):
            df = df.drop_duplicates()

        na_action = st.selectbox("处理空白格：", ["不处理", "删除有空白的行", "把空白填为 0", "填为列的平均值"])
        if na_action == "删除有空白的行":
            df = df.dropna()
        elif na_action == "把空白填为 0":
            df = df.fillna(0)
        elif na_action == "填为列的平均值":
            # 只对数字列填充平均值
            df = df.fillna(df.select_dtypes(include=[np.number]).mean())

        if st.checkbox("清除所有文本的首尾空格"):
            for col in df.select_dtypes(include=['object']).columns:
                df[col] = df[col].astype(str).str.strip()

        # 4. 文本批量替换
        st.markdown("---")
        st.subheader("🔄 文本批量替换")
        replace_col = st.selectbox("选择要替换的列：", ["不替换"] + columns)
        replace_old = st.text_input("要查找的文本（例如：'元'）")
        replace_new = st.text_input("替换为（例如：留空）")
        if replace_col != "不替换" and replace_old:
            df[replace_col] = df[replace_col].astype(str).str.replace(replace_old, replace_new, regex=False)

        # 5. 保留/删除列
        st.markdown("---")
        st.subheader("🗂️ 列管理")
        selected_cols = st.multiselect("选择你想保留的列：", df.columns.tolist(), default=df.columns.tolist())
        if selected_cols:
            df = df[selected_cols]

        # 6. 排序
        st.markdown("---")
        st.subheader("🔢 排序")
        sort_col = st.selectbox("选择按哪一列排序：", ["不排序"] + df.columns.tolist())
        if sort_col != "不排序":
            sort_order = st.radio("排序方式：", ["降序", "升序"], horizontal=True)
            df = df.sort_values(by=sort_col, ascending=(sort_order == "升序"))

        # 7. 高级：自定义计算列
        st.markdown("---")
        st.subheader("🧮 自定义计算")
        current_cols = df.columns.tolist()
        calc_c1, calc_c2, calc_c3 = st.columns(3)
        col_a = calc_c1.selectbox("列A", ["不计算"] + current_cols)
        op = calc_c2.selectbox("操作", ["+", "-", "*", "/"])
        col_b = calc_c3.selectbox("列B", ["不计算"] + current_cols)
        if col_a != "不计算" and col_b != "不计算":
            try:
                if op == "+":
                    df["计算结果"] = df[col_a] + df[col_b]
                elif op == "-":
                    df["计算结果"] = df[col_a] - df[col_b]
                elif op == "*":
                    df["计算结果"] = df[col_a] * df[col_b]
                elif op == "/":
                    df["计算结果"] = df[col_a] / df[col_b]
            except Exception:
                st.error("计算失败：请确保选择的是数字列。")

        # 8. 高级：动态条件筛选
        st.markdown("---")
        st.subheader("🔍 动态筛选")
        st.caption("例如：`分数 > 80` 或 `班级 == '一班'`")
        query_str = st.text_input("输入筛选条件：")
        if query_str:
            try:
                df = df.query(query_str)
            except Exception as e:
                st.error(f"语法错误：{e}")

        # 9. 分组聚合 (Groupby)
        st.markdown("---")
        st.subheader("📈 分组统计")
        group_col = st.selectbox("按哪一列分组？", ["不分组"] + df.select_dtypes(include=['object']).columns.tolist())
        agg_col = st.selectbox("对哪一列进行统计？", ["不统计"] + df.select_dtypes(include=[np.number]).columns.tolist())
        agg_func = st.selectbox("统计方式：", ["求和", "平均值", "最大值", "计数"])
        if group_col != "不分组" and agg_col != "不统计":
            func_map = {"求和": "sum", "平均值": "mean", "最大值": "max", "计数": "count"}
            # 这里为了展示，我们把统计结果生成一个新的表格，不覆盖原表
            grouped_df = df.groupby(group_col)[agg_col].agg(func_map[agg_func]).reset_index()
            st.info("💡 分组统计结果已生成，请查看右侧或下方。")

# ================= 主展示区 =================
if uploaded_file is not None:
    st.subheader("✨ 实时处理结果")

    # 用标签页展示数据，更加高级
    tab1, tab2 = st.tabs(["📄 数据预览", "📈 分组统计结果 (如有)"])

    with tab1:
        st.dataframe(df, width="stretch")

        # 导出功能
        st.markdown("---")
        col_exp1, col_exp2 = st.columns(2)
        with col_exp1:
            # 导出 Excel
            output_excel = io.BytesIO()
            with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
                df.to_excel(writer, index=False)
            st.download_button(
                label="📥 下载为 Excel 文件",
                data=output_excel.getvalue(),
                file_name="清洗后数据.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                type="primary",
                use_container_width=True
            )
        with col_exp2:
            # 导出 CSV
            csv_data = df.to_csv(index=False).encode('utf-8-sig')  # utf-8-sig 防止 Excel 打开乱码
            st.download_button(
                label="📥 下载为 CSV 文件",
                data=csv_data,
                file_name="清洗后数据.csv",
                mime="text/csv",
                use_container_width=True
            )

    with tab2:
        if 'grouped_df' in locals():
            st.dataframe(grouped_df, width="stretch")
        else:
            st.info("请在左侧选择分组列和统计列。")
else:
    # 未上传文件时的提示
    st.info("👈 请在左侧上传文件以开始处理。")
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1000&auto=format&fit=crop",
             caption="让数据清洗变得像呼吸一样简单。", use_container_width=True)