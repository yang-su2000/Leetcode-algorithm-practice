class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s2 = s[::-1]
        if s == s2:
            return s
        n = len(s)
        m = int(1e9+9)
        
        def rolling_pw(m, p=31):
            pw = [0] * n
            pw[0] = p
            for i in range(1, n):
                pw[i] = (pw[i-1] * p) % m
            return pw
        
        def rolling_hash(s, m, pw):
            h = [0] * n
            for i, c in enumerate(s):
                c = ord(c) - ord('a') + 1
                h[i] = c * pw[i]
                if i > 0:
                    h[i] += h[i-1]
                h[i] %= m
            return h
        
        pw = rolling_pw(m)
        prefix_h = rolling_hash(s, m, pw)
        suffix_h = rolling_hash(s2, m, pw)
        
        for add in range(1, n):
            r = (n + add + 1) // 2
            l = r - add
            # print(add, l, r)
            pre = (prefix_h[l-1] * pw[add-1] + suffix_h[add-1]) % m
            suf = suffix_h[r-1]
            if pre == suf:
                return s2[:add] + s
        return s2 + s