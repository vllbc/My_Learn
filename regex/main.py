import plotly
import plotly.graph_objects as go
import numpy as np
def sigmod(x):
    return 1/(1+np.exp(-x))
liss = np.linspace(-10,10,1000)
y = [sigmod(x) for x in liss]
scatter = go.Scatter(x = liss,y = y,mode="lines")
fig = go.Figure(scatter)
fig.show()
