class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s =[]
        for i in nums:
            s.append(int(str(i)[::-1]))
        a = nums+s
        return len(set(a))
        