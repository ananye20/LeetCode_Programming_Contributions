class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int("".join(map(str, digits)))
        new = n+1
        snew = str(new)
        l2=[]
        l = list(snew)
        l2 = list(map(int,l))
        return l2

        