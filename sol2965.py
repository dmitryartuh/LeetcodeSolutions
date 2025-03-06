class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = set()
        a = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] not in s:
                    s.add(grid[i][j])
                    continue
                else:
                    a = grid[i][j]
            
        for i in range(1, len(grid) * len(grid) + 1):
            if i not in s:
                return [a, i]
        
        return [a, 0]