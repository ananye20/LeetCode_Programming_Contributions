class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        l2=[]
        if target not in nums:
            return [-1,-1]
        else:
            for i in range(0, len(nums)):
                if(nums[i]==target):
                    l.append(i)
            l2.append(l[0])
            l2.append(l[-1])
            return l2
            

                
