class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l=[]
        for i in accounts:
            p = sum(i)
            l.append(p)
        return max(l)

        