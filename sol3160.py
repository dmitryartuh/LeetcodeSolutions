class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        d = defaultdict(int)
        d[0] = limit + 1
        color = defaultdict(int)
        res = [0] * (len(queries) + 1)
        for i in range(len(queries)):
            old = color.get(queries[i][0], 0)
            color[queries[i][0]] = queries[i][1]
            new = queries[i][1]
            res[i + 1] = res[i]

            d[old] -= 1
            if old != 0 and d[old] == 0:
                res[i + 1] -= 1

            d[new] += 1
            if new != 0 and d[new] == 1:
                res[i + 1] += 1
        return res[1:]