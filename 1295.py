class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if self.numberCount(num) % 2 == 0:
                res += 1
        
        return res
        
    def numberCount(self, x: int) -> int:
        res = 0
        while x > 0:
            res += 1
            x //= 10

        return res