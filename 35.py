class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if m == r and target > nums[m]:
                return m + 1
            if target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return m
