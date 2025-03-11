class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a = b = c = 0
        i = j = 0
        res = 0
        while (a == 0 or b == 0 or c == 0) and i < len(s):
            if s[i] == 'a':
                a += 1
            elif s[i] == 'b':
                b += 1
            elif s[i] == 'c':
                c += 1
            while a > 0 and b > 0 and c > 0:
                if s[j] == 'a':
                    a -= 1
                elif s[j] == 'b':
                    b -= 1
                elif s[j] == 'c':
                    c -= 1
                j += 1
                res += len(s) - i
            i += 1

        return res
