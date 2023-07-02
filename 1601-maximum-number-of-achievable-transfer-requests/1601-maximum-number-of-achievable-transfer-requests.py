class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        ans = 0
        for i in range((1 << m) - 1, 0, -1):
            cur = bin(i).count('1')
            if cur < ans:
                continue
            in_ = [0] * n
            out_ = [0] * n
            for j in range(m):
                if i & (1 << j):
                    a, b = requests[j]
                    in_[b] += 1
                    out_[a] += 1
            if in_ == out_:
                ans = max(ans, cur)
        return ans