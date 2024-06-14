class Solution:
    def generateParenthesis(self, n: int):
        # 5 = ((((())))) + (4+1) + (3+2) + (2+3) + (1+4)
        
        if n == 1:
            return ["()"]

        special = ""
        for x in range(0, n):
            special += "("
        for x in range(0,n):
            special+= ")"
        combos = [special]
        for x in range(1, (n+1)//2+1):
            leftCombos = self.generateParenthesis(x)
            rightCombos = self.generateParenthesis(n-x)
            for l in leftCombos:
                for r in rightCombos:
                    
                    combos.append(r+l)
        return combos
    
bob = Solution()
print(bob.generateParenthesis(3))