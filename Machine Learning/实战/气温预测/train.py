import torch
from torch.utils.data import DataLoader, TensorDataset
import torch.nn as nn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


EPOCH = 100
BATCH_SIZE = 32
LR = 1e-3

# 定义模型
class Net(nn.Module):
    def __init__(self, in_dim, n_hidden_1, n_hidden_2, n_hidden_3, out_dim):
        super().__init__()
        self.hidden1 = nn.Linear(in_dim, n_hidden_1)
        self.A1 = nn.ReLU()
        self.hidden2 = nn.Linear(n_hidden_1, n_hidden_2)
        self.A2 = nn.ReLU()
        self.hidden3 = nn.Linear(n_hidden_2, n_hidden_3)
        self.A3 = nn.ReLU()
        self.out = nn.Linear(n_hidden_3, out_dim)

    def forward(self, x):
        out = self.A1(self.hidden1(x))
        out = self.A2(self.hidden2(out))
        out = self.A3(self.hidden3(out))
        out = self.out(out)
        return out


net = Net(in_dim=12, n_hidden_1=64, n_hidden_2=32, n_hidden_3=16, out_dim=1)


data = pd.read_csv("气温数据.csv")
data = pd.get_dummies(data)


X = data[data.columns.difference(["actual"])].values
y = data["actual"].values

X = torch.from_numpy(X).float()
y = torch.from_numpy(y.reshape(-1, 1)).float()


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=233)
train_dataset = TensorDataset(X_train, y_train)

train_data = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)

loss_func = nn.MSELoss()
optimizer = torch.optim.Adam(net.parameters(), lr=LR)

# 训练
train_loss, test_loss = [], []
for epoch in range(EPOCH):
    for i, (X_batch, y_batch) in enumerate(train_data):
        predict = net(X_batch)
        loss = loss_func(predict, y_batch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    train_loss.append(loss_func(net(X_train), y_train).item())
    test_loss.append(loss_func(net(X_test), y_test).item())
    print(
        f"Epoch: {epoch+1}, train loss: {train_loss[-1]:.4f}, test loss: {test_loss[-1]:.4f}")
print('final epoch: train loss', train_loss[-1], 'test loss', test_loss[-1])

# 保存训练好的模型
torch.save(net.state_dict(), "202011110014.pth")

# 画图
plt.figure(figsize=(10, 5))
plt.plot(np.arange(1, EPOCH+1), train_loss, label='train loss')
plt.plot(np.arange(1, EPOCH+1), test_loss, label='test loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.show()
