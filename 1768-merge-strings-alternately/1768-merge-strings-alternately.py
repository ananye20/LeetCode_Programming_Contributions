from collections import defaultdict
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        o=[]
        l = min(len(word1), len(word2))

        for i in range(l):
            o.append(word1[i])
            o.append(word2[i])

        o.append(word1[l:])
        o.append(word2[l:])

        return "".join(o)
