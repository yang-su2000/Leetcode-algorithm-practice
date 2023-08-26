class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        ans = 0
        last = -1001
        for a, b in pairs:
            if last < a:
                ans += 1
                last = b
        return ans