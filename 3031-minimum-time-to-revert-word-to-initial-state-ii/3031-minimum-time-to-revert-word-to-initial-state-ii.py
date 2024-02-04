class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
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
        
        n = len(word)
        m = int(1e9+9)
        pw = rolling_pw(n, m)
        h = rolling_hash(word, m, pw)
        
        n = len(word)
        ans = 0
        for i in range(k, n, k):
            ans += 1
            i2 = n - i
            pre = h[i-1] # word[:i]
            suf = (h[n-1] - h[n-i-1] * pw[i-1]) % m # word[n-i:] = hash(word) - hash(word[:n-i]) * power^(i)
            if pre == suf:
                return ans
        return ans + 1