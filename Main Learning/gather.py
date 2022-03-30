# import torch


# Y = torch.tensor([[0.1, 0.3, 0.6], [0.3, 0.2, 0.5]])
# y1 = torch.LongTensor([0,2])
# y2 = torch.LongTensor([0,1,1])
# print(Y.gather(1,y1.view(-1,1))) # gather第一个参数dim=1，指定的是列，也就是要舍弃列，保留行
# print(Y.gather(0,y2.view(1,-1))) # gather第一个参数dim=0，指定的是行，也就是要舍弃行，保留列
# # 简单理解就是说dim=0就是按列进行操作,dim=1就是按行进行操作
# print((Y.argmax(dim=1) == y1).float().mean().item())
# print((Y.argmax(dim=1) == y1).sum().item() / y1.shape[0])

# axis同理  axis=0 指定为行 就是沿着行变化的方向进行操作，注意是变化的方向。也就是要舍弃行 保留列
# axis=1 指定为列，就是沿着列变化的方向进行操作，也就是舍弃列 保留行


import torch
t = torch.Tensor([[1,2],[3,4]])
# t = 1 2
#     3 4
index = torch.LongTensor([[0,0],[1,0]])
# index = 0 0
#         1 0
# dim = 0 : [[1,2],[3,2]]
# dim = 1 : [[1,1],[4,3]]

# index = 0     
#         1
# dim = 0 : [[1],[3]]
# dim = 1 : [[1],[4]]

# index = 0 1
# dim = 0 : [[1, 4]]
# dim = 1 : [[1, 2]]
print(torch.gather(t, 0, index))  # dim = 0     t和index都要按列进行操作
print(torch.gather(t, 1, index))  # dim = 1     t和index都要按行进行操作

# 最终shape为index的shape
assert(index.shape == torch.gather(t, 0, index).shape)

