class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = set()
        for i in range(len(nums)):
            if nums[i] == key:
                j = i
                while j >= 0 and i - j <= k:
                    res.add(j)
                    j -= 1
                j = i
                while j < len(nums) and j - i <= k:
                    res.add(j)
                    j += 1
        
        res = list(res)
        res.sort()

        return res