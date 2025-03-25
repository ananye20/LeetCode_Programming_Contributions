class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)

        prefSum, res, n = 0, 0, len(satisfaction)
        for i in range(n):
            prefSum += satisfaction[i]
            if prefSum < 0:
                break
            res += prefSum

        return res