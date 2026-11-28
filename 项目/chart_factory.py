import matplotlib.pyplot as plt
import seaborn as sns

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def generate_plot(df, chart_type, x_col, y_col):
    fig, ax = plt.subplots(figsize=(10, 5))
    try:
        if chart_type == "柱状图":
            sns.barplot(data=df, x=x_col, y=y_col, ax=ax)
        elif chart_type == "折线图":
            sns.lineplot(data=df, x=x_col, y=y_col, ax=ax)
        elif chart_type == "散点图":
            sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
        elif chart_type == "箱线图":
            sns.boxplot(data=df, x=x_col, y=y_col, ax=ax)

        plt.xticks(rotation=45)
        return fig, None
    except Exception as e:
        return None, str(e)