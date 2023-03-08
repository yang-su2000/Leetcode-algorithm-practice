class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def getTime(k):
            ret = 0
            for p in piles:
                ret += p // k + (p % k > 0)
            return ret
        
        l = 1
        r = 10**9
        while l < r:
            mid = (l + r) // 2
            t = getTime(mid)
            if t > h:
                l = mid + 1
            else:
                r = mid
        return l