class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        d = defaultdict(int)
        for i in arr:
            d[i + diff] = max(d[i + diff], d[i] + 1)
        return max(d.values())