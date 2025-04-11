class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ORD_0 = ord('0')
        res = 0
        for i in range(low, high + 1):
            s = str(i)
            if len(s) % 2 == 1:
                continue
            x1 = x2 = 0
            for j in range(len(s) // 2):
                x1 += int(s[j])
            for j in range(len(s) // 2, len(s)):
                x2 += int(s[j])
            if x1 == x2:
                res += 1

        return res