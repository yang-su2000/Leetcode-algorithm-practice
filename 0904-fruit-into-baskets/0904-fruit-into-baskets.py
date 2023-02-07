class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        t1, t2 = -1, -1
        c1, c2 = 0, 0
        tl = -1
        cl = 0
        ans = 0
        for t in fruits:
            if t1 == t:
                c1 += 1
            elif t2 == t:
                c2 += 1
            elif t1 == -1:
                t1 = t
                c1 = 1
            elif t2 == -1:
                t2 = t
                c2 = 1
            else:
                ans = max(ans, c1 + c2)
                t1 = tl
                c1 = cl
                t2 = t
                c2 = 1
            if tl == -1 or tl != t:
                tl = t
                cl = 1
            else:
                cl += 1
            print(t, ans)
        return max(ans, c1 + c2)