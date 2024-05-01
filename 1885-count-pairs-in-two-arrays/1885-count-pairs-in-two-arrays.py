from sortedcontainers import SortedList

class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        d1 = [x - y for x, y in zip(nums1, nums2)][::-1]
        d2 = [-x for x in d1]
        s = SortedList()
        ans = 0
        for x, y in zip(d1, d2):
            ans += s.bisect_left(x)
            s.add(y)
        return ans