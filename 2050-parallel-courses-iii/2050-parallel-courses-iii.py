class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        A = [[] for _ in range(n)]
        p = [0] * n
        time2 = time.copy()
        for a, b in relations:
            a -= 1
            b -= 1
            A[a].append(b)
            p[b] += 1
        ans = 0
        cur = [] # (time, i)
        for i in range(n):
            if not p[i]:
                heappush(cur, (time2[i], i))
        # print(cur)
        while cur:
            t, i = heappop(cur)
            ans = max(ans, t)
            for child in A[i]:
                p[child] -= 1
                time2[child] = max(time2[child], time[child] + time2[i])
                if not p[child]:
                    heappush(cur, (time2[child], child))
        return ans