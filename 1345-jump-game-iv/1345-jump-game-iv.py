class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        vis = [False] * n
        vis[0] = True
        q = [0]
        d = defaultdict(list)
        for i in range(n):
            d[arr[i]].append(i)
        ans = -1
        while q:
            ans += 1
            q2 = []
            for i in q:
                if i == n-1:
                    return ans
                if i > 0 and not vis[i-1]:
                    q2.append(i-1)
                    vis[i-1] = True
                if i < n-1 and not vis[i+1]:
                    q2.append(i+1)
                    vis[i+1] = True
                for j in d[arr[i]]:
                    if not vis[j]:
                        q2.append(j)
                        vis[j] = True
                d[arr[i]].clear() # crucial optim step to avoid checking all same value again
            q = q2
        return -1 # not found, unreachable