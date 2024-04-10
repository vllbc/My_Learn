import torch.nn as nn
import torch
import pandas as pd

epochs = 100
lr =0.01

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.l1 = nn.Linear(1, 12)
        self.a1 = nn.ReLU()
        self.l2 = nn.Linear(12, 1)
    
    def forward(self, x):
        x = self.l1(x)
        x = self.a1(x)
        output = self.l2(x)
        return output
data = pd.read_excel("./a1d1.xlsx")

a1 = data["a1"].values
day = 1
X = torch.FloatTensor(a1[:-day].reshape(-1, 1))
y = torch.FloatTensor(a1[day:].reshape(-1, 1))

model = Model()
optimizer = torch.optim.Adam(model.parameters(), lr=lr)
loss_func = nn.MSELoss()

for epoch in range(epochs):
    optimizer.zero_grad()
    out = model(X)
    loss = loss_func(out, y)
    loss.backward()
    optimizer.step()
    print(f"epoch: {epoch}, loss: {loss.detach().numpy()}")

