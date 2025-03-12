class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums2 = nums+[]
        mx = max(nums)
        nums.remove(mx)
        mx2 = max(nums)
        if(mx>=2*mx2):
            return nums2.index(mx)
        else:
            return -1

        