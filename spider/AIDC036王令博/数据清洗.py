import pandas as pd

data = pd.read_csv("小火花数据中心.csv")
def replace(x): return x.replace("万+", "0000")


data["粉丝数"] = data["粉丝数"].apply(replace)
data["阅读数"] = data["阅读数"].apply(replace)

data.to_csv("数据清洗.csv", index=False, encoding="utf-8")
