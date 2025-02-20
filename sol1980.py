class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ss = set(nums)
        n = len(nums)

        def find(s) -> str:
            if len(s) == n:
                if s not in ss:
                    return s
                else:
                    return ''

            res = find(s + '0')
            if len(res) > 0:
                return res
            
            res = find(s + '1')
            if len(res) > 0:
                return res

            return ''

        return find('')