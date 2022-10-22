class Solution:
    def minWindow(self, s: str, t: str) -> str:
        q = deque() # (char, idx)
        t = Counter(t)
        d = defaultdict(int)
        count = 0
        i, j = 0, 0
        ans = len(s) + 1
        ret = ''
        while True:
            # find valid
            while j < len(s) and count < len(t):
                c = s[j]
                if c in t:
                    q.append((c, j))
                    d[c] += 1
                    if d[c] == t[c]:
                        count += 1
                j += 1
            if count < len(t):
                break
            # remove overhead
            while q:
                c, i = q[0]
                if d[c] - 1 >= t[c]:
                    q.popleft()
                    d[c] -= 1
                else:
                    break
            # add new ans
            if q:
                i = q[0][1]
            else:
                i = j - 1
            if j - i < ans:
                ans = j - i
                ret = s[i:j]
            # remove first
            if q:
                c, i = q.popleft()
                d[c] -= 1
                count -= 1
            # print(ret)
        return ret