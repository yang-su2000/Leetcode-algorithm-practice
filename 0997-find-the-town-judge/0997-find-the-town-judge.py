class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        t = [0] * (n + 1)
        bt = [0] * (n + 1)
        for a, b in trust:
            t[a] += 1
            bt[b] += 1
        for i in range(1, n + 1):
            if t[i] == 0 and bt[i] == n - 1:
                return i
        return -1