class Solution:
    def minCostClimbingStairs(cost):
        res = [] #res[i]就是到第i阶梯时最小的花费
        res.append(cost[0])  #到第一阶梯最小就是0+cost[0]
        res.append(cost[1]) #第二阶梯最小就是0+cost[1]
        #状态转移方程:res[i] = min(res[i-1],res[i-2])+cost[i]
        for i in range(2,len(cost)): 
            res.append(min(res[i-1],res[i-2])+cost[i]) #
        return min(res[-1],res[-2])