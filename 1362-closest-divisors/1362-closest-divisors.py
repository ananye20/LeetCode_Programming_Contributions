class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for i in reversed(range(1, int((num + 2) ** 0.5) + 1)):
            if not (num + 1) % i:
                return [i, (num + 1) // i]
            if not (num + 2) % i:
                return [i, (num + 2) // i]
