class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            s = str(num)
            l = list(s)
            int_list = list(map(int,l))
            num = sum(int_list)
        return num
        