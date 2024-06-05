class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d = [Counter(w) for w in words]
        di = d[0]
        for counter in d:
            di &= counter
        return di.elements()