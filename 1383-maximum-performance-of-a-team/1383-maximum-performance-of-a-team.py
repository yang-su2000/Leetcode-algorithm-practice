from sortedcontainers import SortedList

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        z = sorted(zip(efficiency, speed), reverse=True)
        spq = [] # speed pirority queue
        ssum, ans = 0, 0 # speed sum, ans
        for e, s in z: # decreasing efficiency, speed
            if len(spq) >= k:
                ssum -= heapq.heappop(spq) # pop min speed
            heapq.heappush(spq, s) # add current speed
            # with the engineer at current speed and efficiency (1) ******
            # find at least more efficient engineers (2) -> max speed sum
            ssum += s
            ans = max(ans, ssum * e)
        return ans % (10**9+7)
    