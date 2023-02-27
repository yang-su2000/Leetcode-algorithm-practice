"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        return self.rec(grid, 0, n-1, 0, n-1)
    
    def rec(self, grid, lrow, rrow, lcol, rcol):
        # print(lrow, rrow, lcol, rcol)
        if lrow == rrow and lcol == rcol:
            is_leaf = True
            val = (grid[lrow][lcol] == 1)
            return Node(val, is_leaf, None, None, None)
        count = 0
        empty = True
        full = True
        for i in range(lrow, rrow + 1):
            for j in range(lcol, rcol + 1):
                if grid[i][j]:
                    empty = False
                    count += 1
                else:
                    full = False
        is_leaf = (empty or full)
        val = (not empty)
        if not is_leaf:
            topleft = self.rec(grid, lrow, (lrow + rrow) // 2, lcol, (lcol + rcol) // 2)
            topright = self.rec(grid, lrow, (lrow + rrow) // 2, (lcol + rcol + 1) // 2, rcol)
            bottomleft = self.rec(grid, (lrow + rrow + 1) // 2, rrow, lcol, (lcol + rcol) // 2)
            bottomright = self.rec(grid, (lrow + rrow + 1) // 2, rrow, (lcol + rcol + 1) // 2, rcol)
            return Node(val, is_leaf, topleft, topright, bottomleft, bottomright)
        return Node(val, is_leaf, None, None, None, None)
    