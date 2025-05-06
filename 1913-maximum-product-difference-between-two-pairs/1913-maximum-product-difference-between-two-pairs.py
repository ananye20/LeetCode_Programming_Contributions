class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a = max(nums)
        nums.remove(max(nums))
        b = max(nums)
        nums.remove(max(nums))
        m1 = a*b
        c = min(nums)
        nums.remove(min(nums))
        d = min(nums)
        nums.remove(min(nums))
        m2 = c*d
        return m1-m2