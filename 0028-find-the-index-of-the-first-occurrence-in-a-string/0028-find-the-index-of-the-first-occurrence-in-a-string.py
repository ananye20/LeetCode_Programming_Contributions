class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(needle in haystack):
            return haystack.index(needle,0,len(haystack))
        else:
            return -1
        