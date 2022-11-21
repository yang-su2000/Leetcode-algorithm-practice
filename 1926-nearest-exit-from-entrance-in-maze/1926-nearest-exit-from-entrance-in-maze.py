class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        q = [entrance]
        d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        steps = 0
        while q:
            q2 = []
            for i, j in q:
                for di, dj in d:
                    i2, j2 = i+di, j+dj
                    if [i2, j2] != entrance and 0 <= i2 < m and 0 <= j2 < n and maze[i2][j2] == '.':
                        if i2 == 0 or i2 == m - 1 or j2 == 0 or j2 == n - 1:
                            return steps + 1
                        maze[i2][j2] = '+'
                        q2.append([i2, j2])
            q = q2
            steps += 1
        return -1
                    