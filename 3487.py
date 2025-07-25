class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set()
        res = 0
        count = 0
        for num in nums:
            if num in s or num <= 0:
                continue
            count += 1
            res += num
            s.add(num)

        if count == 0:
            return max(nums)

        return res