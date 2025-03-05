class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=[]
        for i in operations:
            if(i == 'C'):
                l.pop()
            elif(i == 'D'):
                l.append(int(l[-1])*2)
            elif(i == '+'):
                l.append(int(l[-1])+int(l[-2]))
            else:
                l.append(int(i))
        return sum(l)

        