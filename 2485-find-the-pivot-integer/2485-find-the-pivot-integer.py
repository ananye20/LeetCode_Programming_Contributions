class Solution:
    def pivotInteger(self, n: int) -> int:
        s=0
        l = [i for i in range(1,n+1)]
        for i in range(len(l)+1):
            if(sum(l[:i])==sum(l[i-1:])):
                return i
        return -1


        


        