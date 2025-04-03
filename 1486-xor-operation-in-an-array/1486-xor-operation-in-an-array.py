class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        l=[]
        for i in range(0, n):
            a = start+ 2*i
            l.append(a)
        o = l[0]
        for i in range(1,len(l)):
            o = o^l[i]
        return o