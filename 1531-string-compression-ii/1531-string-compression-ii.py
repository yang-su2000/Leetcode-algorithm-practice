class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(i, c, count, k):
            if k < 0:
                return float('inf')
            if i == len(s):
                return 0
            delete_c = dp(i+1, c, count, k-1)
            if s[i] == c:
                keep_c = dp(i+1, c, count+1, k) + (count in [1, 9, 99])
            else:
                keep_c = dp(i+1, s[i], 1, k) + 1
            return min(keep_c, delete_c)
        
        return dp(0, '', 0, k)