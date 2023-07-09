class Solution:
    def largestVariance(self, s: str) -> int:
        ls = list(set(s))
        counts = Counter(s)
        ans = 0
        for x in range(len(ls)):
            a = ls[x]
            for y in range(len(ls)):
                if x == y:
                    continue
                b = ls[y]
                a_, b_ = 0, 0
                b2_ = counts[b]
                for i in s:
                    if i == a:
                        a_ += 1
                    elif i == b:
                        b_ += 1
                        b2_ -= 1
                    if a_ < b_ and b2_:
                        a_ = 0
                        b_ = 0
                    if a_ and b_:
                        ans = max(ans, a_ - b_)
        return ans