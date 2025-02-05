# shit solution
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swap0, swap1 = None, None
        swapped = False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if swapped:
                    return False
                if swap0 == None:
                    swap0 = s1[i]
                    swap1 = s2[i]
                elif swap1 != s1[i] or swap0 != s2[i]:
                    return False
                else:
                    swapped = True
        return True if swap0 is None or swapped else False