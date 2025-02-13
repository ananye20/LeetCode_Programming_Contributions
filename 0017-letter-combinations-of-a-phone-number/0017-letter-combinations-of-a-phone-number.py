class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l=[]
        k = [" ","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        for j in range(len(digits)):
            for i in range(len(k)):
                if(int(digits[j])==i):
                    l.append(k[i])
        if(len(l)==2):
            l2=[]
            for i in range(len(l)):
                for j in range(i+1, len(l)):
                    for q in l[i]:
                        for r in l[j]:
                            l2.append(q+r)
        elif(len(l)==0):
            l2=[]
        elif(len(l)==1):
            l2=[]
            for i in l[0]:
                l2.append(i)
        elif(len(l)==3):
            l2=[]
            i=0
            for q in l[i]:
                for r in l[i+1]:
                    for t in l[i+2]:
                        l2.append(q+r+t)
        elif(len(l)==4):
            l2=[]
            i=0
            for q in l[i]:
                for r in l[i+1]:
                    for t in l[i+2]:
                        for m in l[i+3]:
                            l2.append(q+r+t+m)
        return l2




      


        