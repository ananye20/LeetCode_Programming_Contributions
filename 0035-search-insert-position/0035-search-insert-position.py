class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0, len(nums)):
            if(target<=nums[i]):
                return i
                break
        return len(nums)
        

        