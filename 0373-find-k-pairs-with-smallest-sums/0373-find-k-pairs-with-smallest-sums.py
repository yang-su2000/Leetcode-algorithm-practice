from heapq import *

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)
        pq = []
        _12 = [0] * n
        for i in range(n):
            heappush(pq, (nums1[i] + nums2[0], i))
        ans = []
        while k and pq:
            k -= 1
            _, i = heappop(pq)
            ans.append([nums1[i], nums2[_12[i]]])
            _12[i] += 1
            if _12[i] < m:
                heappush(pq, (nums1[i] + nums2[_12[i]], i))
        return ans