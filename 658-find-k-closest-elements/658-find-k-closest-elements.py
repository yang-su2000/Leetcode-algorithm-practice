class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        q = [] # (dist, val)
        n = len(arr)
        for i in arr:
            heapq.heappush(q, (-abs(i - x), -i))
            if len(q) > k:
                heapq.heappop(q)
        return sorted([-i for _, i in q])
            