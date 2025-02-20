class Solution:
    def isHappy(self, n: int) -> bool:
        l=[]

        while n != 1 and n not in l:
            l.append(n) 
            sum1 = 0
            while n > 0:
                digit = n % 10  
                sum1 += digit * digit 
                n //= 10
            n = sum1 
        
        return n == 1 