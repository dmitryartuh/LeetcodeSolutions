class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n
        l = res = 0
        r = maxSum
        while l <= r:
            m = (r-l) // 2 + l
            if self.canBuild(m, n, index, maxSum):
                res = m
                l = m + 1
            else:
                r = m - 1
        return res + 1

    def canBuild(self, x: int, n: int, index: int, maxSum: int) -> bool:
        l = max(0, x - index)
        r = max(0, x - (n - 1 - index))
        res = (x + l) * (x - l + 1 ) / 2
        res += (r + x) * (x - r + 1) / 2
        return res - x <= maxSum