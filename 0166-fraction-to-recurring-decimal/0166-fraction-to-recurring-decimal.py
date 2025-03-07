class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)  # If it's an integer, return directly
        
        sign = '-' if (numerator * denominator) < 0 else ''  # Handle negative numbers
        numerator, denominator = abs(numerator), abs(denominator)  # Work with absolute values
        
        integer_part = str(numerator // denominator)  # Get integer part
        remainder = numerator % denominator  # Get remainder
        
        decimal_part = ""
        remainder_map = {}  # To store remainder positions
        
        while remainder and remainder not in remainder_map:
            remainder_map[remainder] = len(decimal_part)  # Store remainder position
            remainder *= 10
            decimal_part += str(remainder // denominator)  # Append quotient
            remainder %= denominator  # Update remainder
        
        if remainder:  # If remainder repeats
            repeat_index = remainder_map[remainder]
            decimal_part = decimal_part[:repeat_index] + "(" + decimal_part[repeat_index:] + ")"
        
        return sign + integer_part + "." + decimal_part  # Combine all parts
