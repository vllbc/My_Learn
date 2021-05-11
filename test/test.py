# import torch


# Y = torch.tensor([[0.1, 0.3, 0.6], [0.3, 0.2, 0.5]])
# y = torch.LongTensor([0, 2])
# print(Y.gather(1,y.view(-1, 1)))
# print((Y.argmax(dim=1) == y).float().mean().item())
# print((Y.argmax(dim=1) == y).sum().item() / y.shape[0])




import torch
t = torch.Tensor([[1,2],[3,4]])
# t = 1 2
#     3 4
index = torch.LongTensor([[0,0],[1,0]])
# index = 0 0
#         1 0
print(torch.gather(t, 0, index))  # 此时dim = 0
print(torch.gather(t, 1, index))  # dim = 1

