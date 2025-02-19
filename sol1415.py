class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []

        def find(s: str):
            if len(res) == k:
                return
            if len(s) == n:
                res.append(s)
                return

            if s == '' or s[-1] != 'a':
                find(s + 'a')
            
            if s == '' or s[-1] != 'b':
                find(s + 'b')
                
            if s == '' or s[-1] != 'c':
                find(s + 'c')

        find('')

        return res[k-1] if len(res) >= k else ''