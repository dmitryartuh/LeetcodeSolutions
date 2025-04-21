class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_x = upper
        max_x = lower
        current = lower
        for d in differences:
            max_x = max(max_x, current)
            min_x = min(min_x, current)
            current += d        
        
        max_x = max(max_x, current)
        min_x = min(min_x, current)

        lower_delta = lower - min_x
        upper_delta = upper - max_x
        res = upper_delta - lower_delta + 1

        return max(0, res)