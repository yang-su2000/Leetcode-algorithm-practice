class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        @cache
        def dp(uplayed, played):
            return uplayed >= n if played == goal else ((n - uplayed) * dp(uplayed + 1, played + 1) + max(uplayed - k, 0) * dp(uplayed, played + 1)) % (10**9+7)
        return dp(0, 0)