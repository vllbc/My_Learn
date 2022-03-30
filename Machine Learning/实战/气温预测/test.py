import torch
import torch.nn as nn
import numpy as np

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

net = Net(12,64,32,16,1)
net.load_state_dict(torch.load("202011110014.pth"))

month = input("输入月份：")
day = input("输入day：")
week = input("输入星期：")
temp_3 = input("输入前三天气温：")
temp_2 = input("输入前两天气温：")
temp_1 = input("输入前一天气温：")
inputs = [int(month), int(day), int(temp_3), int(temp_2), int(temp_1)]
last_week = np.zeros(7)
last_week[int(week)-1] = 1
inputs.extend(last_week)
inputs = torch.FloatTensor(inputs)

print("当天的气温预测为：", net(inputs))
