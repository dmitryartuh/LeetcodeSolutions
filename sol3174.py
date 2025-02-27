class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        for c in s:
            if c in digits:
                res.pop(-1)
            else:
                res.append(c)

        return ''.join(res){\rtf1} 