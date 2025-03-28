import heapq
from typing import List
import numpy


class Solution:
    def sortFirst(val):
        return val[0]

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        orderedQueries = [0] * len(queries)
        k = 0
        while k < len(queries):
            orderedQueries[k] = [queries[k], k]
            k += 1
        orderedQueries = sorted(orderedQueries, key=lambda x: x[0])

        result = [0] * len(queries)
        h = []
        history = numpy.full((len(grid), len(grid[0])), False)
        heapq.heappush(h, (grid[0][0], 0, 0))
        history[0][0] = True
        sI = len(grid)
        sJ = len(grid[0])

        count = 0
        k = 0
        while len(orderedQueries) > 0 and k < len(queries):
            current = orderedQueries[k]
            while len(h) > 0:
                cel = heapq.heappop(h)
                if (cel[0] >= current[0]):
                    heapq.heappush(h, cel)
                    break
                count += 1
                i = cel[1]
                j = cel[2]
                if i > 0 and history[i - 1, j] == False:
                    heapq.heappush(h, (grid[i - 1][j], i - 1, j))
                    history[i - 1, j] = True

                if j > 0 and history[i, j - 1] == False:
                    heapq.heappush(h, (grid[i][j - 1], i, j - 1))
                    history[i, j - 1] = True

                if i + 1 < sI and history[i + 1, j] == False:
                    heapq.heappush(h, (grid[i + 1][j], i + 1, j))
                    history[i + 1, j] = True

                if j + 1 < sJ and history[i, j + 1] == False:
                    heapq.heappush(h, (grid[i][j + 1], i, j + 1))
                    history[i, j + 1] = True

            result[current[1]] = count
            k += 1

        return result