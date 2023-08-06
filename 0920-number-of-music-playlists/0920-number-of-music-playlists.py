class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        @cache
        def dp(uplayed, played, old):
            return uplayed >= n if played == goal else ((n - uplayed) * dp(uplayed + 1, played + 1, old + (uplayed >= k)) + old * dp(uplayed, played + 1, old)) % (10**9+7)
        return dp(0, 0, 0)