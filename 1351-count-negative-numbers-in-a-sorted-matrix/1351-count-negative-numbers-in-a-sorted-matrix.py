class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        flat_list = sum(grid, [])
        for i in flat_list:
            if(i<0):
                c+=1

        return c
