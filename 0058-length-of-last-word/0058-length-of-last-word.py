class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        res = len(l[-1])
        return res
        