class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        cp=0
        cn=0
        for i in nums:
            if(i>0):
                cp+=1
            elif(i<0):
                cn+=1
        return max(cp,cn)

        