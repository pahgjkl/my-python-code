import streamlit as st
import pandas as pd
from core_engine import apply_basic_cleaning, apply_advanced_processing, merge_tables, create_zip_from_split, \
    get_excel_bytes
from chart_factory import generate_plot

# ================= 页面基础设置 =================
st.set_page_config(page_title="超级数据工作台", page_icon="🚀", layout="wide")
st.title("🚀 超级数据自动化工作台 (Pro Max版)")
st.caption("一站式解决：清洗、VLOOKUP合并、拆分打包、数据透视与可视化。")

# ================= 侧边栏 =================
with st.sidebar:
    st.header("⚙️ 全局设置")
    uploaded_file = st.file_uploader("请上传主 Excel 或 CSV 文件", type=["xlsx", "csv"])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                try:
                    df = pd.read_csv(uploaded_file, encoding='utf-8')
                except UnicodeDecodeError:
                    df = pd.read_csv(uploaded_file, encoding='gbk')
            else:
                df = pd.read_excel(uploaded_file)
            st.success(f"✅ 读取成功: {uploaded_file.name}")
        except Exception as e:
            st.error(f"❌ 读取失败: {e}")
            st.stop()

        processed_df = df.copy()

# ================= 主界面 =================
if uploaded_file is not None:
    tab_clean, tab_advanced, tab_merge, tab_export, tab_visual = st.tabs([
        "🧹 基础清洗", "🧮 高级处理", "🔗 双表合并(VLOOKUP)", "📦 拆分与导出", "📊 可视化图表"
    ])

    # 标签页 1：基础清洗
    with tab_clean:
        st.subheader("数据概览")
        c1, c2, c3 = st.columns(3)
        c1.metric("总行数", len(processed_df))
        c2.metric("总列数", len(processed_df.columns))
        c3.metric("缺失值总计", processed_df.isnull().sum().sum())

        st.markdown("---")
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            if st.checkbox("删除全局完全重复的行"):
                processed_df = processed_df.drop_duplicates()
            na_action = st.selectbox("处理空白值：", ["不处理", "删除包含空白的行", "全部填为 0", "数字列填平均值"])
        with col_c2:
            clear_space = st.checkbox("清除所有文本列的首尾空格")
            lower_text = st.checkbox("全部转换为小写 (针对文本)")

        # 调用引擎
        if st.button("执行基础清洗"):
            processed_df = apply_basic_cleaning(processed_df, na_action, clear_space, lower_text)
            st.success("基础清洗完成！")

    # 标签页 2：高级处理
    with tab_advanced:
        st.subheader("高级去重与替换")
        col_a1, col_a2 = st.columns(2)
        with col_a1:
            dup_cols = st.multiselect("按指定列去重：", processed_df.columns.tolist())
        with col_a2:
            rep_col = st.selectbox("选择要替换的列：", ["不替换"] + processed_df.columns.tolist())
            rep_pattern = st.text_input("查找(支持正则)：")
            rep_new = st.text_input("替换为：")

        st.markdown("---")
        query_str = st.text_input("动态条件筛选 (例如 `成绩 > 80`)：")
        s_col = st.selectbox("选择排序列：", ["不排序"] + processed_df.columns.tolist())
        s_order = st.radio("排序方式：", ["降序", "升序"], horizontal=True)

        # 调用引擎
        if st.button("执行高级处理"):
            processed_df = apply_advanced_processing(processed_df, dup_cols, rep_col, rep_pattern, rep_new, query_str,
                                                     s_col, s_order)
            st.success("高级处理完成！")

    # 标签页 3：合并
    with tab_merge:
        st.subheader("🔗 智能 VLOOKUP")
        file2 = st.file_uploader("上传第二张表", type=["xlsx", "csv"], key="file2")
        if file2 is not None:
            df2 = pd.read_excel(file2) if file2.name.endswith('.xlsx') else pd.read_csv(file2)
            common_cols = list(set(processed_df.columns) & set(df2.columns))

            if common_cols:
                merge_key = st.selectbox("选择共同列：", common_cols)
                merge_type = st.radio("连接方式：", ["左连接(保留主表)", "内连接(只保留匹配)"], horizontal=True)
                if st.button("🚀 执行合并"):
                    processed_df = merge_tables(processed_df, df2, merge_key, merge_type)
                    st.success("合并成功！")
            else:
                st.warning("两表没有名字相同的列。")

    # 标签页 4：拆分与导出
    with tab_export:
        st.subheader("📦 按条件拆分")
        split_col = st.selectbox("选择拆分依据列：", ["不拆分"] + processed_df.columns.tolist())
        if split_col != "不拆分":
            if st.button("生成 ZIP 压缩包"):
                zip_data = create_zip_from_split(processed_df, split_col)
                st.download_button("📥 下载 ZIP", zip_data, "拆分结果.zip", "application/zip")

        st.markdown("---")
        st.subheader("💾 导出当前表")
        col_e1, col_e2 = st.columns(2)
        with col_e1:
            st.download_button("📥 下载 Excel", get_excel_bytes(processed_df), "最终数据.xlsx")
        with col_e2:
            csv_data = processed_df.to_csv(index=False).encode('utf-8-sig')
            st.download_button("📥 下载 CSV", csv_data, "最终数据.csv", "text/csv")

    # 标签页 5：可视化
    with tab_visual:
        st.subheader("📊 自动化图表")
        chart_type = st.selectbox("图表类型：", ["柱状图", "折线图", "散点图", "箱线图"])
        numeric_cols = processed_df.select_dtypes(include=['number']).columns.tolist()

        if numeric_cols:
            c_x = st.selectbox("X 轴：", processed_df.columns.tolist())
            c_y = st.selectbox("Y 轴：", numeric_cols)
            if st.button("生成图表"):
                fig, error = generate_plot(processed_df, chart_type, c_x, c_y)
                if fig:
                    st.pyplot(fig)
                else:
                    st.error(f"画图失败：{error}")
        else:
            st.warning("没有数字列，无法画图。")

    # 全局预览
    st.markdown("---")
    st.subheader("👀 实时数据预览")
    st.dataframe(processed_df.tail(100), use_container_width=True)

else:
    st.info("👈 请在左侧上传文件。")