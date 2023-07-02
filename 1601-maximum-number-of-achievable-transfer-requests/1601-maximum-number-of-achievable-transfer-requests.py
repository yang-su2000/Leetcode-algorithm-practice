class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        ans = 0
        for i in range(1 << m):
            in_ = [0] * n
            out_ = [0] * n
            cur = 0
            for j in range(m):
                if i & (1 << j):
                    a, b = requests[j]
                    in_[b] += 1
                    out_[a] += 1
                    cur += 1
            if in_ == out_:
                ans = max(ans, cur)
        return ans