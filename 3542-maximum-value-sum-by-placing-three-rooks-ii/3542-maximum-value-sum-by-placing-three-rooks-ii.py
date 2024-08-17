class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        top_left = [[-inf] * n for _ in range(m)]
        top_right = [[-inf] * n for _ in range(m)]
        bot_left = [[-inf] * n for _ in range(m)]
        bot_right = [[-inf] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                top_left[r][c] = board[r][c]
                if r:
                    top_left[r][c] = max(top_left[r][c], top_left[r-1][c])
                if c:
                    top_left[r][c] = max(top_left[r][c], top_left[r][c-1])
        for r in range(m-1, -1, -1):
            for c in range(n):
                bot_left[r][c] = board[r][c]
                if r < m-1:
                    bot_left[r][c] = max(bot_left[r][c], bot_left[r+1][c])
                if c:
                    bot_left[r][c] = max(bot_left[r][c], bot_left[r][c-1])
        for r in range(m):
            for c in range(n-1, -1, -1):
                top_right[r][c] = board[r][c]
                if r:
                    top_right[r][c] = max(top_right[r][c], top_right[r-1][c])
                if c < n-1:
                    top_right[r][c] = max(top_right[r][c], top_right[r][c+1])
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                bot_right[r][c] = board[r][c]
                if r < m-1:
                    bot_right[r][c] = max(bot_right[r][c], bot_right[r+1][c])
                if c < n-1:
                    bot_right[r][c] = max(bot_right[r][c], bot_right[r][c+1])
        rmax = [[-inf] * n for _ in range(m)]
        cmax = [[-inf] * n for _ in range(m)]
        rmax2 = [[-inf] * n for _ in range(m)]
        cmax2 = [[-inf] * n for _ in range(m)]
        for r in range(m):
            rmax[r][0] = board[r][0]
            for c in range(1, n):
                rmax[r][c] = max(board[r][c], rmax[r][c-1])
        for c in range(n):
            cmax[0][c] = board[0][c]
            for r in range(1, m):
                cmax[r][c] = max(board[r][c], cmax[r-1][c])
        for r in range(m):
            rmax2[r][-1] = board[r][-1]
            for c in range(n-2, -1, -1):
                rmax2[r][c] = max(board[r][c], rmax2[r][c+1])
        for c in range(n):
            cmax2[-1][c] = board[-1][c]
            for r in range(m-2, -1, -1):
                cmax2[r][c] = max(board[r][c], cmax2[r+1][c])
        # print(top_left)
        # print(top_right)
        # print(bot_left)
        # print(bot_right)
        # print(rmax)
        # print(cmax)
        # print(rmax2)
        # print(cmax2)
        ans = -inf
        for r in range(1, m-1):
            for c in range(1, n-1):
                cur = -inf
                cur = max(cur, board[r][c] + top_left[r-1][c-1] + bot_right[r+1][c+1])
                cur = max(cur, cmax2[r+1][c] + rmax2[r][c+1] + top_left[r-1][c-1])
                cur = max(cur, rmax[r][c-1] + cmax2[r+1][c] + top_right[r-1][c+1])
                cur = max(cur, board[r][c] + top_right[r-1][c+1] + bot_left[r+1][c-1])
                cur = max(cur, cmax[r-1][c] + rmax2[r][c+1] + bot_left[r+1][c-1])
                cur = max(cur, cmax[r-1][c] + rmax[r][c-1] + bot_right[r+1][c+1])
                ans = max(ans, cur)
                # print(r, c, ans)
        return ans