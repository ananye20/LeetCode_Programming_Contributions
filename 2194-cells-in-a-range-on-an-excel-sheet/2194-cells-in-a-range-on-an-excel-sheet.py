class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        abc=[]
        ans = []
        for i in range(65, 91):
            abc.append(chr(i))  
        s1 = s.split(":") 
        start_c = s1[0][0]
        end_c = s1[1][0]
        start_n = s1[0][1]
        end_n = s1[1][1]
        x = abc[abc.index(start_c):abc.index(end_c)+1]
        for j in x:
            for i in range(int(start_n), int(end_n) +1):
                new = j + str(i)
                ans.append(new)
        return ans
            
            