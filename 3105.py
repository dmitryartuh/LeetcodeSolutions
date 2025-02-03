class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 0
        current = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current += 1
            else:
                res = max(res, current)
                current = 1
        res = max(res, current)
        
        current = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                current += 1
            else:
                res = max(res, current)
                current = 1
        res = max(res, current)

        return res