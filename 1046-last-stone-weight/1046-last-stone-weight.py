
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()  
            stone1 = stones.pop()
            stone2 = stones.pop()
            if stone1 != stone2:
                stones.append(stone1 - stone2)
        
        return stones[0] if stones else 0
