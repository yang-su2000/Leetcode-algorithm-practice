class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        for i in nums:
            p = bisect.bisect_left(ans, i)
            if p == len(ans):
                ans.append(i)
            else:
                ans[p] = i
        return len(ans)