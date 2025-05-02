class Solution:
    def sortSentence(self, s: str) -> str:
        l,a=[],[]
        s1 = s.split(" ")
        for i in range(1, len(s1)+1):
            for j in range(0, len(s1)):
                if(str(i) in s1[j]):
                    l.append(s1[j])
        for i in range(0, len(l)):
            l1 = l[i][:-1]
            a.append(l1)
        return " ".join(a)


        