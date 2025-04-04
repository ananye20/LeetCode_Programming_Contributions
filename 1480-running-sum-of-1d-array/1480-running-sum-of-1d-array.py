class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        n = [None]*len(nums)
        for i in range(len(nums)):
            sum+= nums[i]
            n[i] = sum
        return n