class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l=[]
        for let in letters:
            a = ord(target)
            sub = ord(let)-a
            if(sub>0):
                l.append(sub)
        if(l==[]):
            return letters[0]
        else:
            m = min(l)
            return chr(ord(target)+m)

        

        
        



        