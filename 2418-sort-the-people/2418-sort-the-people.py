class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = [None]*len(names)
        h = sorted(heights, reverse = True)
        for i in range(0, len(h)):
            a = heights.index(h[i])
            n[i] = names[a] 
        return n