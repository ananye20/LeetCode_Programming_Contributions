class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = max(nums)-1
        nums.remove(max(nums))
        return m*(max(nums)-1)
        