class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        q = [(days + 1, 0)]
        for m in meetings:
            heapq.heappush(q, (m[0], 0))
            heapq.heappush(q, (m[1], 1))

        res = now = 0
        free_from = 0
        current_m = 0
        while q:
            t, e = heapq.heappop(q)
            if e == 0:
                if current_m == 0:
                    res += t - free_from - 1
                current_m += 1
            else:
                current_m -= 1
                if current_m == 0:
                    free_from = t

        return res