class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if(word.isupper() is True):
            return True
        elif(word.islower() is True):
            return True
        elif(word.istitle() is True):
            return True
        else:
            return False