class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] >= nums[1] + nums[2] or nums[1] >= nums[0] + nums[2] or nums[2] >= nums[0] + nums[1]:
            return 'none'

        s = set(nums)

        if len(s) == 1:
            return 'equilateral'

        if len(s) == 2:
            return 'isosceles'

        return 'scalene'