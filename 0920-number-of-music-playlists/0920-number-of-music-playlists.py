class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9+7
        # number of unique played songs, number of played songs, number of old songs that can be replayed
        @cache
        def dp(uplayed, played, old):
            if played == goal:
                ret = uplayed >= n
            else:
                new_played = (n - uplayed) * dp(uplayed + 1, played + 1, old + (uplayed >= k))
                old_played = old * dp(uplayed, played + 1, old)
                ret = new_played + old_played
            return ret % mod
        
        return dp(0, 0, 0)