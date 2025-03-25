class Solution:
    def checkValidCuts(self, _: int, a: List[List[int]]) -> bool:
        sx,sy,ex,ey = zip(*a)
        return any(sum(starmap(le,zip(accumulate([0,*b],max),a)))>2
            for a,b in starmap(zip,map(sorted,map(zip,(sx,sy),(ex,ey))))
        )