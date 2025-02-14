class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        print(s)
        l = s.split()
        l2 = l[::-1]
        return " ".join(l2)