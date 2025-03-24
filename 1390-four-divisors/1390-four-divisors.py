from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def get_divisors(n):
            divisors = set()
            sqrt_n = int(math.sqrt(n))
            for i in range(1, sqrt_n + 1):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
                if len(divisors) > 4:
                    return []
            return divisors if len(divisors) == 4 else []

        total_sum = 0
        seen = {} 
        for num in nums:
            if num in seen:
                total_sum += seen[num]
            else:
                divisors = get_divisors(num)
                div_sum = sum(divisors) if divisors else 0
                seen[num] = div_sum 
                total_sum += div_sum

        return total_sum
