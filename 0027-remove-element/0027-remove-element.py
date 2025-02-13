class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=0
        for i in nums:
            if(i == val):
                c+=1
        for j in range(0,c):
            nums.remove(val)
        return len(nums)
        
        