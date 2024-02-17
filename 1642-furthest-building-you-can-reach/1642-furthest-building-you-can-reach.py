class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        
        def solve(idx):
            ls = []
            for i in range(idx):
                if heights[i] < heights[i+1]:
                    heappush(ls, heights[i+1] - heights[i])
            b = bricks
            while ls:
                val = heappop(ls)
                if b >= val:
                    b -= val
                else:
                    val -= b
                    heappush(ls, val)
                    break
            return len(ls) <= ladders
        
        while l < r:
            mid = (l + r) // 2 + 1
            if solve(mid):
                l = mid
            else:
                r = mid - 1
        return l