class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        rev=y[::-1]
        if(y==rev):
            return True
        else:
            return False
        