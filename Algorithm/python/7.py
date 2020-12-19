#两个数组的交集
#用了哈希表和Counter

class Solution:
    def intersect(nums1,nums2):
        from collections import Counter
        n1 = Counter(nums1)
        res = []
        for i in nums2:
            if n1.get(i) and n1[i] >0:
                res.append(i)
                n1[i] -= 1
        return res