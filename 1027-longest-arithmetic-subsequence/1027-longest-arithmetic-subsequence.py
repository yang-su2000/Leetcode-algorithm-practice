class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        ans = 2
        n = len(nums)
        ls = [] # idx = diff -> count
        for r in range(n):
            d2 = defaultdict(int)
            for l, d in enumerate(ls):
                diff = nums[r] - nums[l]
                if diff in d:
                    d2[diff] = max(d2[diff], d[diff] + 1)
                else:
                    d2[diff] = 2
                ans = max(ans, d2[diff])
            ls.append(d2)
        return ans