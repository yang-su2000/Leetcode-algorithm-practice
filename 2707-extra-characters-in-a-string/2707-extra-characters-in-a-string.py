class Solution:
    def minExtraChar(self, s: str, ds: List[str]) -> int:
        @cache
        def rec(i):
            if i >= len(s):
                return 0
            ret = 1 + rec(i+1)
            for d in ds:
                if s[i:i+len(d)] == d:
                    ret = min(ret, rec(i+len(d)))
            return ret
            
        return rec(0)