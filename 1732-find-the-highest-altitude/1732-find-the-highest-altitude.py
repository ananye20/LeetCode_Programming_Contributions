class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l,s=[], 0
        for i in gain:
            s+= i
            l.append(s)
        l.append(0)
        return max(l)
            
        