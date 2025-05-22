class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        l=[]
        for i in sentences:
            p = i.split(" ")
            x=len(p)
            l.append(x)
        return max(l)        