class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l = list(str(n))
        p=1
        l1 = list(map(int, l))
        s = sum(l1)
        for i in l1:
            p = p*i
        return p-s
        