class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        if all(d == 0 for d in digits):
            return "0"
        
        digits.sort(reverse=True) 
        s = sum(digits)
        
        r1, r2 = [], []
        for d in digits:
            if d % 3 == 1:
                r1.append(d)
            elif d % 3 == 2:
                r2.append(d)
        
        if s % 3 == 1:
            if r1:
                digits.remove(r1[-1])  
            elif len(r2) > 1:
                digits.remove(r2[-1])
                digits.remove(r2[-2])
        elif s % 3 == 2:
            if r2:
                digits.remove(r2[-1]) 
            elif len(r1) > 1:
                digits.remove(r1[-1])
                digits.remove(r1[-2])
        
        if not digits:
            return ""

        if digits[0] == 0:
            return "0"
        
        return ''.join(map(str, digits))
