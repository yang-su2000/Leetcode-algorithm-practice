from bisect import bisect_right

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        # k -> end, sum
        ls = [(0, 0)]
        for _ in range(k):
            ls2 = []
            for a, b, val in events:
                p = bisect_right(ls, (a, -inf)) - 1
                val2 = ls[p][1] + val
                ls2.append((b, val2))
            ls2.extend(ls)
            ls2.sort()
            ls3 = []
            for end, sval in ls2:
                if not ls3 or (ls3[-1][0] < end and ls3[-1][1] < sval):
                    ls3.append((end, sval))
                elif ls3[-1][0] == end:
                    ls3[-1] = (end, max(ls3[-1][1], sval))
            ls = ls3
            # print(ls)
        return max(sval for _, sval in ls)