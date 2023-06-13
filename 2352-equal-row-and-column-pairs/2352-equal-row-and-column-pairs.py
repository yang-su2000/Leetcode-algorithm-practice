class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = {} # use -1 -> to denote count
        n = len(grid)
        ans = 0
        for row in grid:
            d2 = d
            for val in row:
                if val not in d2:
                    d2[val] = {}
                d2 = d2[val]
            if -1 not in d2:
                d2[-1] = 1
            else:
                d2[-1] += 1
        for i in range(n):
            d2 = d
            for j in range(n):
                val = grid[j][i]
                if val not in d2:
                    d2[val] = {}
                d2 = d2[val]
            if -1 in d2:
                ans += d2[-1]
        return ans
            
                    