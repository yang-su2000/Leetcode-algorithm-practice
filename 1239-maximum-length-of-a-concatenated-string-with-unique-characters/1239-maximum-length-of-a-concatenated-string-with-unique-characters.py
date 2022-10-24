class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [s for s in arr if len(set(s)) == len(s)]
        ans = 0
        
        def bt(i, s):
            nonlocal ans
            if i == len(arr):
                ans = max(ans, len(s))
                return
            s2 = set(arr[i])
            st = s | s2
            if len(st) == len(s) + len(s2):
                bt(i+1, st)
            bt(i+1, s)
        
        bt(0, set())
        return ans