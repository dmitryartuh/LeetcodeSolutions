class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        return self.coloredCells(n - 1) + (n - 1) * 4