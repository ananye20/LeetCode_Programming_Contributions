class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=[]
        for i in s:
            j= i.lower()
            if(j.isalnum()):
                s1.append(j)

        if(s1== s1[::-1]):
            return True
        else:
            return False