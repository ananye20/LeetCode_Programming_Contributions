class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [],[]
        for x in nums:
            if x>0:
                pos.append(x)  
        for x in nums:
            if x<0:
                neg.append(x)
        result = []

        for i in range(len(pos)):
            result.append(pos[i]) 
            result.append(neg[i])  

        return result