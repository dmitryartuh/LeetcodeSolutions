class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        s = set(supplies)
        res = []
        r_with_is = [[recipes[i], ingredients[i]] for i in range(len(recipes))]
        while r_with_is:
            next_r_with_is = []
            for r_with_i in r_with_is:
                canDo = True
                for ing in r_with_i[1]:
                    if ing not in s:
                        canDo = False
                        next_r_with_is.append(r_with_i)
                        break
                if canDo:
                    res.append(r_with_i[0])
                    s.add(r_with_i[0])
            if len(next_r_with_is) < len(r_with_is):
                r_with_is = next_r_with_is
            else:
                break

        return res