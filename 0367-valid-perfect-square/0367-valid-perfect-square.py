class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        nums=(sqrt(num))
        n = round(nums,0)
        return n*n == num
        