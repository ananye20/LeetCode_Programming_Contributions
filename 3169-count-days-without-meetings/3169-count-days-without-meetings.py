from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()  
        merged = []
        
        for start, end in meetings:
            if merged and start <= merged[-1][1]:  
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        
        occupied_days = sum(end - start + 1 for start, end in merged)
        return days - occupied_days
