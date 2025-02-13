class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        
        x_abs_reversed = int(str(abs(x))[::-1])
        
        result = sign * x_abs_reversed
        
        if result < MIN_INT or result > MAX_INT:
            return 0
        
        return result
