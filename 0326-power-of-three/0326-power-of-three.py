class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(0,100):
            if(n == 3**i):
                return True
            elif(n<=0):
                return False
            else:
                continue
        return False
        