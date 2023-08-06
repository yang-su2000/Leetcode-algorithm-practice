class Solution:
    @cache
    def numMusicPlaylists(self, n: int, goal: int, k: int, played: int = 0) -> int:
        return played >= n if not goal else ((n - played) * self.numMusicPlaylists(n, goal - 1, k, played + 1) + max(played - k, 0) * self.numMusicPlaylists(n, goal - 1, k, played)) % (10**9+7)