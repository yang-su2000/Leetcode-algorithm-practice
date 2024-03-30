from sortedcontainers import SortedSet

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        s = SortedSet()
        d = {}
        j = -1
        for i in range(n):
            val = nums[i]
            if val in d:
                s.remove(d[val])
            d[val] = i
            s.add(d[val])
            if len(s) > k:
                j = s.pop(0)
                del d[nums[j]]
            if len(s) == k:
                ans += s[0] - j
            # print(i, s, ans)
        return ans