class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if(len(nums)==len(list(set(nums)))):
            return False
        else:
            return True
        