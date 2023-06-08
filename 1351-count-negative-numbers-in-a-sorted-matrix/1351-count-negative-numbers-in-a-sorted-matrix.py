class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(bisect.bisect_left(grid[i][::-1], 0) for i in range(len(grid)))