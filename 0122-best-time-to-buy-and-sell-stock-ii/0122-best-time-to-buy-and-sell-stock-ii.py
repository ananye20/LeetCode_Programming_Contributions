class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        for i in range(len(prices)-1):
            x = prices[i+1]-prices[i]
            if x>0:
                prof+=x
        return prof