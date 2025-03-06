from statistics import mode

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return mode(nums)


        