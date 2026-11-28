import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# 【核心修改】直接指向服务器上字体文件的绝对路径
font_path = "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"
try:
    # 强行让 matplotlib 加载这个字体
    my_font = fm.FontProperties(fname=font_path)
    # 并且全局设置为默认字体（防止其他地方乱码）
    plt.rcParams['font.sans-serif'] = [my_font.get_name()]
    plt.rcParams['axes.unicode_minus'] = False
except Exception:
    # 如果本地跑没这个路径，就用本地系统默认的（防止本地报错）
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