from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        l=[]

        for s in strs:
            sorted_s = tuple(sorted(s))
            ana[sorted_s].append(s)

        for i in ana.values():
            l.append(i)
        
        return l
