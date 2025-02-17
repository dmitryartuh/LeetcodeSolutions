class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        s = set()
        c = Counter(tiles)
        
        def find(a: str, i: int):
            if len(a) > 0 and a not in s:
                s.add(a)

            if i == len(tiles):
                return            

            find(a, i + 1)
            
            for key in c.keys():
                if c[key] == 0:
                    continue
                c[key] -= 1
                find(a + key, i + 1)
                c[key] += 1

        find('', 0)

        return len(s)