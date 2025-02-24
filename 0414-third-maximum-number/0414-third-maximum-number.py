class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        sorted_unique_nums = sorted(unique_nums, reverse=True)

        if len(sorted_unique_nums) >= 3:
            return sorted_unique_nums[2]
        
        return sorted_unique_nums[0]