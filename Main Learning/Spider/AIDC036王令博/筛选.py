import pandas as pd

data = pd.read_csv("数据清洗.csv")

res_data = data[data["评论数"].apply(lambda x:int(x) > 2000)]
res_data.to_csv("评论大于2000.csv", index=False, encoding="utf-8")
