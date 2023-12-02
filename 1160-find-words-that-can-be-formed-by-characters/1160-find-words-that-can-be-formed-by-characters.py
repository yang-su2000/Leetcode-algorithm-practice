class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)
        ans = 0
        for w in words:
            if Counter(w) <= c:
                ans += len(w)
        return ans