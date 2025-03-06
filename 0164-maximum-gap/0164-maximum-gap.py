class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        md=0
        if(len(nums)<2):
            return 0
        elif(len(nums)==2):
            return max(nums)-min(nums)
        else:
            nums.sort()
            for i in range(0, len(nums)-1):
                d = nums[i+1]-nums[i]
                if(d>md):
                    md=d
            return md


                