class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]
        for i in range(left, right+1):
            stringi = str(i)
            c=0
            for j in stringi:
                a = int(j)
                if(a!=0 and i%a == 0):
                    c+=1
                    if(c == len(stringi)):
                        l.append(i)
        return l

        