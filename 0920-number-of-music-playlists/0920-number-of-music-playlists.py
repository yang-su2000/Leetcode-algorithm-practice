class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9+7
        # k = 5, n = 10, goal = 20
        # 1, 2, 3, 4, 5, 6, 7, 1, 2/3
        # 1, 2, 3, 4, 5, 6, 7, 2, 1/3
        # cand <= chosen <= n
        # played <= goal
        @cache
        def dp(chosen, played, cand):
            if played == goal:
                ret = chosen >= n
            else:
                ret = (n - chosen) * dp(chosen + 1, played + 1, cand + (chosen >= k)) + cand * dp(chosen, played + 1, cand)
            # print(chosen, played, cand, ret)
            return ret % mod
        
        return dp(0, 0, 0)