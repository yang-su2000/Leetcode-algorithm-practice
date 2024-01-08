class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # return self.shortestPalindrome_rolling_hash(s)
        return self.shortestPalindrome_KMP(s)
    
    def shortestPalindrome_KMP(self, s: str) -> str:
        
        def KMP(s):
            n = len(s)
            p = [0] * n
            for i in range(1, n):
                j = p[i-1]
                while j and s[i] != s[j]:
                    j = p[j-1]
                if s[i] == s[j]:
                    j += 1
                p[i] = j
            return p
        
        s2 = s[::-1]
        s_total = s + "#" + s2
        prefix_func = KMP(s_total)
        l = prefix_func[-1]
        return s2[:len(s)-l] + s
    
    def shortestPalindrome_rolling_hash(self, s: str) -> str:
        s2 = s[::-1]
        if s == s2:
            return s
        
        def rolling_pw(n, m, p=31):
            pw = [0] * n
            pw[0] = p
            for i in range(1, n):
                pw[i] = (pw[i-1] * p) % m
            return pw
        
        def rolling_hash(s, m, pw):
            h = [0] * len(s)
            for i, c in enumerate(s):
                c = ord(c) - ord('a') + 1
                h[i] = c * pw[i]
                if i > 0:
                    h[i] += h[i-1]
                h[i] %= m
            return h
        
        n = len(s)
        m = int(1e9+9)
        pw = rolling_pw(n, m)
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