class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        iSet = set()
        jSet = set()
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    iSet.add(i)
                    jSet.add(j)        
        for i in range(n):
            for j in range(m):
                if i in iSet or j in jSet:
                    matrix[i][j] = 0