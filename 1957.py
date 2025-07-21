class Solution:
    def makeFancyString(self, s: str) -> str:
        res = [s[0]]
        current = s[0]
        count = 1
        for i in range(1, len(s)):
            if s[i] != current:
                count = 1
                current = s[i]
                res.append(s[i])
                continue
            if count == 2:
                continue
            res.append(s[i])
            count += 1
        
        return ''.join(res)