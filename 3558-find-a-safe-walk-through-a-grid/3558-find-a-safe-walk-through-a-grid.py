class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[-1 for _ in range(n)] for _ in range(m)]
        initial_health = health - grid[0][0]
        if initial_health <=0:
            return False
        visited[0][0] = initial_health

        queue = deque()
        queue.append((0, 0, initial_health))
        while queue:
            x, y, current_health = queue.popleft()
            if x == m - 1 and y == n - 1:
                return True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_health = current_health - grid[nx][ny]
                    if new_health <=0:
                        continue
                    if new_health > visited[nx][ny]:
                        visited[nx][ny] = new_health
                        queue.append((nx, ny, new_health))
        return False