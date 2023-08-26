class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        @cache
        def dp(i):
            ret = 0
            a, b = pairs[i]
            for j, (c, d) in enumerate(pairs):
                if b < c:
                    ret = max(ret, dp(j))
            return ret + 1
        return max(dp(i) for i in range(len(pairs)))