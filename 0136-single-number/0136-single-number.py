class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            for j in nums:
                if(i==j):
                    c+=1
            if(c==1):
                return i
            else:
                c=0

        