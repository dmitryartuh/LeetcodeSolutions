class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = [1]
        num = 1
        for i in range(len(pattern)):
            num += 1
            if pattern[i] == 'I':
                res.append(num)
            else:
                j = i
                x = num
                while j >= 0 and pattern[j] != 'I':
                    res[j] += 1
                    x -= 1
                    j -= 1
                res.append(x)
        ord_0 = ord('0')

        return ''.join([chr(ord_0 + a) for a in res])