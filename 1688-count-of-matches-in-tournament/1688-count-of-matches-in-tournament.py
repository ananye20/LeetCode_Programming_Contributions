class Solution:
    def numberOfMatches(self, n: int) -> int:
        s=0
        while(n>1):
            if(n%2==0):
                matches = n//2
                s = s+matches
                advance = n//2
                n = advance
            else:
                matches = (n-1)//2
                s = s+matches
                advance = (n-1)//2 + 1
                n = advance
        return s
                

        