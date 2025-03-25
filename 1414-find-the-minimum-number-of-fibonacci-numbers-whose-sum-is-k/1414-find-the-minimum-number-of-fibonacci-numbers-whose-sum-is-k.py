class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]  
        while fib[-1] + fib[-2] <= k:
            fib.append(fib[-1] + fib[-2])

        fib = fib[::-1] 
        count = 0
        for num in fib:
            if k >= num: 
                k -= num 
                count+= 1  
            if k == 0:  
                break
        return count
