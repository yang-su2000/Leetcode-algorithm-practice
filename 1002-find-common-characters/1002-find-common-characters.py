class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d = [Counter(w) for w in words]
        di = d[0]
        for counter in d:
            di &= counter
        ans = []
        for c, count in di.items():
            ans.extend([c] * count)
        return ans