class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        d = defaultdict(int)
        l = 0
        count = 0
        for r in range(n):
            d[nums[r]] += 1
            if d[nums[r]] == 1:
                k -= 1
            if k < 0:
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    k += 1
                l += 1
                count = 0
            if k == 0:
                while d[nums[l]] > 1:
                    d[nums[l]] -= 1
                    l += 1
                    count += 1
                ans += count + 1
        return ans