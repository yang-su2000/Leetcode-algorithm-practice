class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def getTrips(t):
            ret = 0
            for ti in time:
                ret += t // ti
            return ret
        
        l = 0
        r = 10**14
        while l < r:
            mid = (l + r) // 2
            trips = getTrips(mid)
            if trips < totalTrips:
                l = mid + 1
            else:
                r = mid
        return l