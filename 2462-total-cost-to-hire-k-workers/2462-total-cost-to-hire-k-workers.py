from heapq import *

class Solution:
    def totalCost(self, costs: List[int], k: int, cand: int) -> int:
        n = len(costs)
        l = cand - 1
        r = n - cand
        pq = []
        for i in range(n):
            if i <= l:
                heappush(pq, (costs[i], 1))
            elif r <= i:
                heappush(pq, (costs[i], 2))
        # print(pq)
        ans = 0
        while k:
            k -= 1
            val, group = heappop(pq)
            ans += val
            if l + 1 >= r:
                continue
            if group == 1:
                l += 1
                heappush(pq, (costs[l], 1))
            else:
                r -= 1
                heappush(pq, (costs[r], 2))
        return ans