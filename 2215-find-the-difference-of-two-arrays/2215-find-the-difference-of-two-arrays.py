class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        d1 = [False] * 2001
        d2 = [False] * 2001
        for i in nums1:
            d1[i+1000] = True
        for i in nums2:
            d2[i+1000] = True
        ans = [[], []]
        for i in range(2001):
            if d1[i] and not d2[i]:
                ans[0].append(i-1000)
            if not d1[i] and d2[i]:
                ans[1].append(i-1000)
        return ans