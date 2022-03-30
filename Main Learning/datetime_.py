import datetime

now = datetime.datetime.now()
# shengri = datetime.datetime(2002,12,17)
# days = (now - shengri)
print(now.strftime('%H:%M:%S'))
# strftime 根据给定的格式将对象转换为字符串
# strptime 将字符串解析为给定相应格式的 datetime 对象
import matplotlib.pyplot as plt
import numpy as np

def show_data_by_condition(df, colname="Total Price", method="sum"):
    """[summary]

    Args:
        df ([type]): [dataframe]
        colname (str, optional): [the column name]. Defaults to "Total Price".
        method (str, optional): [the function]. Defaults to "sum".
    """    
    def transform(df):
        return df.groupby("Order Date")[colname].agg(method)

    res = df.groupby("Item Name").apply(transform).transpose()
    width = 0.1
    plt.figure(figsize=(14, 7))
    for index, column_name in enumerate(res):
        plt.bar(np.arange((len(res.index))) + index * width,
                res[column_name],
                width=width,
                label=column_name + " " + colname)
    plt.xticks(
        np.arange((len(res.index))) + (width * (len(res.columns) - 1)) / 2,
        res.index)
    plt.legend()
    plt.show()

