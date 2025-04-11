class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        cmax=0
        for i in s:
            if(i =="("):
                c+=1
                if(c>cmax):
                    cmax=c
            elif(i == ")"):
                c-=1
        return cmax
        
        