class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n = len(workers)
        m = len(bikes)
        def d(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        ls = [(d(workers[i], bikes[j]), i, j) for i in range(n) for j in range(m)]
        ans = [-1] * n
        taken = [-1] * m
        for _, i, j in sorted(ls):
            if ans[i] == -1 and taken[j] == -1:
                ans[i] = j
                taken[j] = i
        return ans