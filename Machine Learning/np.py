import numpy as np
import operator
group = np.array([[1,101],[5,89],[108,5],[115,8]])
    #四组特征的标签
labels = ['爱情片','爱情片','动作片','动作片']
ceshi = np.array([[100,10]])
ce1 = np.tile(ceshi,(group.shape[0],1)) - group
oreder = ce1**2
adds = oreder.sum(1)
last = adds**0.5#[134.46932736 123.55565548   9.43398113  15.13274595]

nums = last.argsort()#[2 3 1 0]
labelss = {}
for i in range(3):
    las_nm = labels[nums[i]]
    
    labelss[las_nm] = labelss.get(las_nm,0) + 1
    

sorts = sorted(labelss.items(),key=operator.itemgetter(1),reverse=True)
print(sorts[0][0])





