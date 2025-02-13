class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0
        while nums:
            x = heapq.heappop(nums)
            if x >= k:
                return res
            y = heapq.heappop(nums)
            z = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, z)
            res += 1

        return -1