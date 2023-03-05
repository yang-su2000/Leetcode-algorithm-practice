class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0] * n # 0 unvisit, 1 in visit, 2 done visit
        dp[0] = 1
        q = [0]
        d = defaultdict(list)
        for i in range(n):
            d[arr[i]].append(i)
        ans = -1
        while q:
            # print(q)
            ans += 1
            q2 = []
            for i in q:
                if i == n-1:
                    return ans
                if dp[i] == 2:
                    continue
                dp[i] = 2
                if i > 0 and dp[i-1] == 0:
                    q2.append(i-1)
                    dp[i-1] = 1
                if i < n-1 and dp[i+1] == 0:
                    q2.append(i+1)
                    dp[i+1] = 1
                for j in d[arr[i]]:
                    if dp[j] == 0:
                        q2.append(j)
                        dp[j] = 1
                d[arr[i]].clear()
            q = q2
        return -1 # not found, unreachable