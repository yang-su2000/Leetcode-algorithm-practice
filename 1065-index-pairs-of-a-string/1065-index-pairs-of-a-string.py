class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []
        n = len(text)
        for word in words:
            m = len(word)
            for i in range(n - m + 1):
                if word == text[i: i+m]:
                    ans.append([i, i+m-1])
        return sorted(ans)