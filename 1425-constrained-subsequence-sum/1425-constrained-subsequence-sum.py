class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        st = deque([0]) # (idx w/ decreasing value)
        n = len(nums)
        dp = [0] * n # dp[i] must choose idx i
        for i in range(n):
            while st and st[0] < i - k:
                st.popleft()
            dp[i] = max(0, (dp[st[0]] if st else 0)) + nums[i]
            while st and dp[st[-1]] <= dp[i]:
                st.pop()
            st.append(i)
        return max(dp)