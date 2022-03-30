# class Solution:
#     def maxSubArray(nums):
#         res = -float('inf')
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 res = max(res,sum(nums[i:j+1]))
#         return res

class Solution:
    def maxSubArray(nums):
        for i in range(1,len(nums)):
            maxs = max(nums[i-1]+nums[i],nums[i])
            nums[i] = maxs
        return max(nums)