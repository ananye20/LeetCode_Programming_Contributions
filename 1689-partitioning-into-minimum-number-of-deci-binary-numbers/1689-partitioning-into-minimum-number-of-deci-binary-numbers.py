class Solution:
    def minPartitions(self, n: str) -> int:
        n1 = list(n)
        n2 = list(map(int, n1))
        return max(n2)

        