class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)
        for i in range(1, n + 1):
            groups[self.getGroup(i)] += 1

        m = 0
        res = 0
        for k in groups.keys():
            if groups[k] > m:
                m = groups[k]
                res = 1
            elif groups[k] == m:
                res += 1

        return res

    def getGroup(self, x: int) -> int:
        res = 0
        while x > 0:
            res += x % 10
            x //= 10

        return res