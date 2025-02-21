class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(0,100):
            if(n == 4**i):
                return True
            else:
                continue
            return False
        