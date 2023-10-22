class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        st = deque([0]) # (idx w/ decreasing value)
        n = len(nums)
        ans = nums[0]
        dp = [0] * n # must choose i
        dp[0] = nums[0]
        for i in range(1, n):
            while st and st[0] < i - k:
                st.popleft()
            dp[i] = max(0, dp[st[0]] if st else 0) + nums[i]
            while st and dp[st[-1]] <= dp[i]:
                st.pop()
            st.append(i)
            ans = max(ans, dp[i])
            # print(i, st)
        # print(dp)
        return ans