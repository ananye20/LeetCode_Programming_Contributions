class Solution:
    def isValid(self, s: str) -> bool:
        p = -1  
        while len(s) != p: 
            p = len(s)
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
        return len(s) == 0