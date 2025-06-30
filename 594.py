class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        res = 0
        for num, count in counts.items():
            if num+1 in counts:
                res = max(res, count + counts[num+1])
        return res