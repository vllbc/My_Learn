import plotly.graph_objects as go
import pandas as pd
from collections import Counter

# 读取爬取的数据
datas = pd.read_csv("datas.csv", encoding="ANSI")
press = datas["出版社"]
counter = Counter(press)
bar = go.Bar(x=list(counter.keys()), y=list(counter.values()))
figure = go.Figure(bar)
figure.update_layout(
    title="柱状图",
    yaxis_title="数量"
)
figure.show()
