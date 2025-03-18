class Solution:
    def longestNiceSubarray(self, nums):
        n, left, right, maxi, mask = len(nums), 0, 0, 0, 0
        while right < n:
            while (mask & nums[right]) != 0:
                mask -= nums[left]
                left += 1
            mask += nums[right]
            maxi = max(maxi, right - left + 1)
            right += 1
        return maxi