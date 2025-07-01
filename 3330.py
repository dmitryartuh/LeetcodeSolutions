class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        c = word[0]
        for i in range(1, len(word)):
            if c == word[i]:
                res += 1
            else:
                c = word[i]

        return res