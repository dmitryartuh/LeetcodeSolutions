class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        
        a = [0] * n
        a[0] = 1
        a[1] = 2
        a[2] = 5
        i = 3
        while i < n:
            a[i] = (a[i - 1] * 2 + a[i - 3]) % 1000000007
            i += 1

        return a[n - 1]