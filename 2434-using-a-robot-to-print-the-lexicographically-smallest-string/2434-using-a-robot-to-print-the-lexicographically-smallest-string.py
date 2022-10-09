class Solution:
    def robotWithString(self, s: str) -> str:
        t = []
        ans = []
        c = 'a'
        while c <= 'z':
            while t and t[-1] <= c:
                ans.append(t.pop())
            t2 = []
            for i in s:
                if i != c:
                    t2.append(i)
                else:
                    t += t2
                    t2 = []
                    ans.append(i)
            s = t2
            c = chr(ord(c) + 1)
            # print(s, t, ans)
        return ''.join(ans + t[::-1])
            