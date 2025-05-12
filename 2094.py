class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i == j or i == k or j == k or digits[i] == 0:
                        continue
                    a = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if a % 2 == 0 and a not in res:
                        res.add(a)

        return sorted(list(res))