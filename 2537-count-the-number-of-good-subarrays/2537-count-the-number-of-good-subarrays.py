class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ans = 0
        i = -1
        j = 0
        n = len(nums)
        d = defaultdict(int)
        count = 0
        while i < n:
            if i >= 0:
                cur = nums[i]
                d[cur] -= 1
                count -= d[cur]
            i += 1
            # print(i, j, count, d)
            while j < n and count < k:
                cur = nums[j]
                count += d[cur]
                d[cur] += 1
                j += 1
                # print(i, j, count, d)
            if count >= k:
                ans += n - j + 1
            # print(ans)
        return ans