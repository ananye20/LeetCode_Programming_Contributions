class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n1 = nums[0:n]
        n2 = nums[n:len(nums)]
        n3 = []
        for i in range(n):
            n3.append(n1[i])
            n3.append(n2[i])
        return n3


        