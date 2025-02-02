from typing import List

# todo
class Solution930:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        current = 0
        i = j = 0
        res = 0
        while i < len(nums) and j < len(nums):
            # find last 1 for get goal
            while j < len(nums) and goal > current:
                current += nums[j]
                j += 1
            if goal > current:
                break
            # find the next 1
            res += 1
            while j < len(nums) and current + nums[j] == goal:
                res += 1
                j += 1
            # find the first 1 in subarray
            while i < j and current - nums[i] == goal:
                res += 1
                i += 1
            i += 1
            current -= 1
        return res