import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ls = []
        n = len(nums1)
        for i in range(n):
            ls.append((nums2[i], nums1[i]))
        ls.sort(reverse=True)
        csum = 0
        ans = 0
        pq = []
        for i in range(k):
            a2, a1 = ls[i]
            csum += a1
            heappush(pq, a1)
        ans = ls[k-1][0] * csum
        for i in range(k, n):
            a2, a1 = ls[i]
            csum += a1
            heappush(pq, a1)
            csum -= heappop(pq)
            ans = max(ans, a2 * csum)
        return ans
        