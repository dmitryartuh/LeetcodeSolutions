class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for num in nums:
            v = num
            score = 0
            while num > 0:
                score += num % 10
                num //= 10
            d[score].append(v)

        res = -1
        for key in d.keys():
            pool = d[key]
            if len(pool) <= 1:
                continue
            m1 = pool[0]
            i1 = 0
            for i in range(len(pool)):
                if m1 < pool[i]:
                    m1 = pool[i]
                    i1 = i
            m2 = pool[(i1 + 1) % len(pool)]
            for i in range(len(pool)):
                if m2 < pool[i] and i != i1:
                    m2 = pool[i]
            res = max(res, m1 + m2)

        return res