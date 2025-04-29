class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        c=0
        if(ruleKey == "type"):
            a=0
        elif(ruleKey == "color"):
            a = 1
        elif(ruleKey == "name"):
            a = 2
        for i in range(len(items)):
            if(items[i][a]== ruleValue):
                c+=1
            else:
                continue
        return c

        