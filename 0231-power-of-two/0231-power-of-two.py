class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(0,100):
            if(n== 2**i):
                return True
            else:
                continue
            return False
        