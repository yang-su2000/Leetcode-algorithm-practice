class Solution:
    def insert(self, ls: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, j = newInterval
        l, r = [], []
        for a, b in ls:
            if b < i:
                l.append([a, b])
            elif a > j:
                r.append([a, b])
            else:
                i = min(i, a)
                j = max(j, b)
        return l + [[i, j]] + r
            