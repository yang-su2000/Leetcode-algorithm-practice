class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        
        def rec(ls, sub):
            nonlocal ans
            if sub == '':
                ans.append(' '.join(ls))
                return
            for word in wordDict:
                if len(sub) >= len(word) and sub[:len(word)] == word:
                    ls.append(word)
                    rec(ls, sub[len(word):])
                    ls.pop()
        
        rec([], s)
        return ans