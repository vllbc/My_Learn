#简单的贪婪问题

class Solution:
    def maxProfit(prices):
        lirun = 0
        for i in range(1,len(prices)):
            zhuan = prices[i] - prices[i-1]
            if zhuan > 0:
                lirun += zhuan
        return lirun

print(Solution.maxProfit([7,1,5,3,6,4]))