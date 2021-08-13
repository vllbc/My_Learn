import plotly.graph_objects as go
import pandas as pd

# 读取爬取的数据
datas = pd.read_csv("datas.csv", encoding="ANSI")

scatter = go.Scatter(x=datas["标题"],y=datas["评分"],mode="markers")
figure = go.Figure(scatter)
figure.update_layout(
    title="散点图",
    xaxis_title="书名",
    yaxis_title="评分"
)
figure.show()