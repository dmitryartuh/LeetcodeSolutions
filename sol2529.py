class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n and nums[i] < 0:
            i += 1
        neg = i
        while i < n and nums[i] == 0:
            i += 1
        return max(neg, n - i)
        