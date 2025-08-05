class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = 0
        for f in fruits:
            res += 1
            for i in range(len(baskets)):
                if baskets[i] >= f:
                    res -= 1
                    baskets[i] = 0
                    break

        return res