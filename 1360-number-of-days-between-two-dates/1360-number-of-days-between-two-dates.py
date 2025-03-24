from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        Date1 = datetime.strptime(date1, "%Y-%m-%d")
        Date2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs((Date2 - Date1).days)