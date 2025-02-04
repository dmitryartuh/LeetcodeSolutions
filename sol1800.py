class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        r = res
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                r += nums[i]
            else:
                res = max(res, r)
                r = nums[i]

        return max(res, r)