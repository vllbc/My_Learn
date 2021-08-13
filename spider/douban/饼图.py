import plotly.graph_objects as go
import pandas as pd
from collections import Counter
# 读取爬取的数据
datas = pd.read_csv("datas.csv", encoding="ANSI")
scores = datas["评分"]
last_scores = []
for s in scores:
    if s != "评价人数少于10人":
        last_scores.append(float(s))
counter = Counter(map(int,last_scores))
pie = go.Pie(labels=list(counter.keys()), values=list(counter.values()))
figure = go.Figure(pie)
figure.update_layout(
    title="评分占比"
)
figure.show()
