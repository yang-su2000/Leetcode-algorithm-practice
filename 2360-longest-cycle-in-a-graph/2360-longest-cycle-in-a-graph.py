class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        vis = [-1] * n
        ans = -1
        time = 0
        for i in range(n):
            ctime = time
            cur = i
            while vis[cur] == -1:
                vis[cur] = time
                time += 1
                cur = edges[cur]
                if cur == -1:
                    break
                if vis[cur] >= ctime:
                    ans = max(ans, time - vis[cur])
                    break
        # print(vis)
        return ans