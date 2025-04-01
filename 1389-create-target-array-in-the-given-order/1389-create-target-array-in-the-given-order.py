class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        output = []
        
        for i in range(len(nums)):
            value = nums[i]
            idx = index[i]
            
            output.insert(idx, value)
        
        return output