class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if(dividend>0 and divisor>0):
            return dividend//divisor
        elif(dividend == -2147483648 and divisor == -1 ):
            return 2147483647 
        elif(dividend<0 and divisor>0):
            d = -(dividend)
            return -(d//divisor)
        elif(divisor<0 and dividend>0):
            dv = -(divisor)
            return -(dividend//dv)
        elif(divisor<0 and dividend<0):
            return dividend//divisor   
        else:
            return 0