class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            val = self.minCost(mid, chargeTimes, runningCosts)
            if val <= budget:
                l = mid + 1
            else:
                r = mid - 1
        return r
    
    def minCost(self, k, charge, cost):
        q = [(-charge[i], i) for i in range(k)]
        heapify(q)
        c = k * sum(cost[:k])
        ans = -q[0][0] + c
        for i in range(k, len(charge)):
            while q and -q[0][0] > -charge[i]:
                if q[0][1] <= i - k:
                    heapq.heappop(q)
                else:
                    break
            heapq.heappush(q, (-charge[i], i))
            c = c - k * cost[i-k] + k * cost[i]
            ans = min(ans, -q[0][0] + c)
        return ans