class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        result = 10000
        bestA = bestB = None
        primeA = primeB = None
        for i in range(max(2, left), right + 1):
            if self.isPrime(i):
                primeA = primeB
                primeB = i
                if primeA is not None and primeB is not None:
                    if primeB - primeA < result:
                        result = primeB - primeA
                        if result == 1 or result == 2:
                            return [primeA, primeB]
                        bestA = primeA
                        bestB = primeB
        if result == 10000:
            return [-1, -1]
        return [bestA, bestB]


    def isPrime(self, n: int):
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True