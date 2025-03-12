class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        c=1
        maxc=1
        for i in range(0, len(nums)-1):
            if(nums[i]<nums[i+1]):
                c+=1
            else:
                maxc = max(maxc,c)
                c=1
        return max(maxc, c)