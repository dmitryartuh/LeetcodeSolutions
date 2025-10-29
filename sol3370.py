class Solution:
    def smallestNumber(self, n: int) -> int:
        b = 0
        x = 2 ** b
        while x <= n:
            b += 1
            x *= 2

        res = 0
        for i in range(b):
            res += 2 ** i

        return res