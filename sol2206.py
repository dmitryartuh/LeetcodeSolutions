class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for k in counter.keys():
            if counter[k] % 2 == 1:
                return False

        return True