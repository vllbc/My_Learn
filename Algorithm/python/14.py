#动态规划问题，写的比较蠢，出了两次错才把特例写上。。

class Solution:
    def rob(nums):
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        maxs = []
        maxs.append(nums[0])
        maxs.append(nums[1])
        for i in range(2,len(nums)):
            maxs.append(max(maxs[:i-1])+nums[i])
        return max(maxs)