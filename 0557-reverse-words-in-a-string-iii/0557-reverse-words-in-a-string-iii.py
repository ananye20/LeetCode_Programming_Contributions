class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        l2=[]
        for i in l:
            l2.append(i[::-1])
        return " ".join(l2)

        