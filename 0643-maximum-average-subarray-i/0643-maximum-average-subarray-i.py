class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w = sum(nums[:k])
        max_w = w

        for i in range(k, len(nums)):
            w+= nums[i]-nums[i-k]
            max_w = max(max_w, w)

        return max_w/k
