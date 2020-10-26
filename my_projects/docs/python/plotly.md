# plotly学习：

```python
import plotly.graph_objects as go
```

是画图的主要库

```python
go.Scatter()
```

画点或者画线
在`Scatter()`中传入`mode='markers’`即可创建散点图
`go.Bar()`建立柱状图
`import plotly.express as px`
`fig  = px.scatter(,,color='Name')`

改变不同点的颜色

**fig是先用go.Scatter()建立的对象**

plotly画图的一般步骤
1.导入模块：
`import plotly`

`import plotly.graph_objects as go`

`import pandas`



2.用pandas读入csv文件
`data = pandas.read_csv('')`



3.选择建立的图标类型，是柱状图，还是散点图，还是折线图，还是3d图。





4.以折线图为例
`scatter = go.Scatter(x='x轴数据',y=‘y轴数据’，name='图例名称')`

`fg = go.Figure(scatter)`

`fg.show()`

ps:若要建立多个图例的表，需要以下操作。
`scatter1=go.....`

`scatter2=go.....`

`........`

`scattern=go.....`

`fg = go.Figure((scatter1,scatter2......))`



可以用循环写入
最后

`fg.show()`



5.注意的地方：
柱状图注意要显示每个柱子上面的数字的话要加上`text`参数，然后令`textposition`参数的值为`outside`