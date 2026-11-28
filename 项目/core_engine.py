import pandas as pd
import numpy as np
import io
import zipfile


def apply_basic_cleaning(df, na_action, clear_space, lower_text):
    # 清除空格
    if clear_space:
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].astype(str).str.strip()
    # 转小写
    if lower_text:
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].str.lower()

    # 处理空值
    if na_action == "删除包含空白的行":
        df = df.dropna()
    elif na_action == "全部填为 0":
        df = df.fillna(0)
    elif na_action == "数字列填平均值":
        df = df.fillna(df.select_dtypes(include=[np.number]).mean())
    return df


def apply_advanced_processing(df, dup_cols, rep_col, rep_pattern, rep_new, query_str, s_col, s_order):
    # 指定列去重
    if dup_cols:
        df = df.drop_duplicates(subset=dup_cols, keep='first')

    # 正则替换
    if rep_col != "不替换" and rep_pattern:
        df[rep_col] = df[rep_col].astype(str).str.replace(rep_pattern, rep_new, regex=True)

    # 筛选
    if query_str:
        try:
            df = df.query(query_str)
        except Exception:
            pass  # 如果筛选出错就不处理，界面会提示

    # 排序
    if s_col != "不排序":
        df = df.sort_values(by=s_col, ascending=(s_order == "升序"))

    return df


def merge_tables(df1, df2, merge_key, merge_type):
    how = 'left' if "左连接" in merge_type else 'inner'
    return pd.merge(df1, df2, on=merge_key, how=how)


def create_zip_from_split(df, split_col):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for name, group in df.groupby(split_col):
            excel_buffer = io.BytesIO()
            group.to_excel(excel_buffer, index=False, engine='openpyxl')
            safe_name = str(name).replace('/', '_')
            zip_file.writestr(f"{safe_name}.xlsx", excel_buffer.getvalue())
    return zip_buffer.getvalue()


def get_excel_bytes(df):
    out_ex = io.BytesIO()
    with pd.ExcelWriter(out_ex, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)
    return out_ex.getvalue()