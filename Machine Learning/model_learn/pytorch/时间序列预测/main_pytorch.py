# import torch.nn as nn
# import torch
# import torchvision
# import pandas as pd

# epochs = 100
# lr =0.01

# class Model(nn.Module):
#     def __init__(self):
#         super(Model, self).__init__()
#         self.l1 = nn.Linear(1, 12)
#         self.a1 = nn.ReLU()
#         self.l2 = nn.Linear(12, 1)
    
#     def forward(self, x):
#         x = self.l1(x)
#         x = self.a1(x)
#         output = self.l2(x)
#         return output
# data = pd.read_excel("./a1d1.xlsx")

# a1 = data["a1"].values
# day = 1
# X = torch.FloatTensor(a1[:-day].reshape(-1, 1))
# y = torch.FloatTensor(a1[day:].reshape(-1, 1))

# model = Model()
# optimizer = torch.optim.Adam(model.parameters(), lr=lr)
# loss_func = nn.MSELoss()

# for epoch in range(epochs):
#     optimizer.zero_grad()
#     out = model(X)
#     loss = loss_func(out, y)
#     loss.backward()
#     optimizer.step()
#     print(f"epoch: {epoch}, loss: {loss.detach().numpy()}")

'''
Author:
SID:
Unikey:
'''
import sys
height = int(input("Enter height of triangle: "))
character = input("Character: ")
if character.strip() == "":
    character = "*"
elif len(character) > 1:
    character = character[0]
if height ==0:
    print("")
if height == 1:
    print(" {} ".format(character))
    sys.exit()
height = 3 if height < 0 else height  
for i in range(2 * height + 1):
    if i == height:
        print(character, end="")
    else:
        print(" ", end="")
print()
for j in range(height-1, 1, -1):
    for i in range(2 * height+1):
        if i == j:
            print(character, end="")
        elif i == 2* height - j:
            print(character, end="")
        else:
            print(" ", end="")
    print()

for i in range(2 * height + 1):
    if i == 0 or i == 2 * height:
        print(" ", end="")
    else:
        print(character, end="")
