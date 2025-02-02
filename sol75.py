from typing import List


class Solution75:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        x = 0
        while i < len(nums):
            while i < len(nums) and nums[i] == x:
                i += 1
            j = max(j, i + 1)
            while j < len(nums):
                if nums[j] == x:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    j += 1
                    break
                j += 1
            if j == len(nums):
                if nums[i] == x:
                    i += 1
                x += 1
                j = i + 1

