class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        res = 0
        i = 0
        start = 0
        while i < len(nums):
            if nums[i] in s:
                res = max(res, sum(s))
                while start < i and nums[start] != nums[i]:
                    s.remove(nums[start])
                    start += 1
                start += 1
            s.add(nums[i])
            i += 1

        res = max(res, sum(s))

        return res