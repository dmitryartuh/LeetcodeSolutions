class Solution:
    def candy(self, ratings: List[int]) -> int:
        r_i = [(ratings[i], i) for i in range(len(ratings))]
        res = [1] * len(ratings)
        r_i.sort()
        for (r, i) in r_i:
            if i > 0 and ratings[i-1] > ratings[i]:
                res[i-1] = max(res[i-1], res[i] + 1)
            if i + 1 < len(ratings) and ratings[i+1] > ratings[i]:
                res[i+1] = max(res[i+1], res[i] + 1)

        return sum(res)
            