class Solution:
    def myAtoi(self, s: str) -> int:
        isNegative = False
        index = 0
        while index<len(s):
            if s[index] == "-":
                isNegative = True
            try:
                int(s[index])
                break
            except:
                index+=1
        
        num = 0
        while index<len(s):
            try:
                int(s[index])
            except:
                break
            num=num*10+int(s[index])
            index+=1
        
        if isNegative:
            num=num*-1
            if num<=-2**31:
                return -2**31
            return num
        if num>=2**31-1:
            return 2**31-1
        return num
        
bob = Solution()
print(bob.myAtoi("42"))