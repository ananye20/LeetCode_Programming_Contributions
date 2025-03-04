class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u,d,le,r =0,0,0,0
        l = list(moves)
        for i in l:
            if(i == "U"):
                u+=1
            elif(i == "D"):
                d+=1
            elif(i == "L"):
                le+=1
            elif(i == "R"):
                r+=1
        if(r == le and u==d):
            return True
        else:
            return False