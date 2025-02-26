class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"  
        
        is_negative = num < 0  
        num = abs(num)
        
        l = []
        while num > 0:
            remainder = num % 7 
            l.append(str(remainder))  
            num = num // 7 
        
        l.reverse() 
        
        if is_negative:
            return "-" + "".join(l)  
        else:
            return "".join(l) 