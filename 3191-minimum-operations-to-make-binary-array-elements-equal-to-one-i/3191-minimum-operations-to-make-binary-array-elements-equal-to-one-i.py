class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0 # number of flips done
        flip1 = flip2 = False # true/false flip at i + 1 and i + 2
        
        for i in range(n - 2):
            # if num = 0 = flip = false or num = 1 = flip = true, result is 0 and need to flip again to get 1
            need_flip = nums[i] == flip1

            flip1, flip2 = flip2, False # move flip to next index

            if need_flip:
                count += 1 # need another flip for current num
                flip1, flip2 = not flip1, not flip2 # flip at i + 1 and i + 2          

        # if num != flip at index then will have 1 as final num
        # if last two nums are 1, all nums are 1 and return count. else, impossible to make all 1, return -1
        return count if nums[n - 2] != flip1 and nums[n - 1] != flip2 else -1