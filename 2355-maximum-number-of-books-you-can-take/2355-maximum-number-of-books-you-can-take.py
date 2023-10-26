class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        dp = [0] * n
        st = [] # idx
        for i, val in enumerate(books):
            while st and books[st[-1]] > val - (i - st[-1]):
                st.pop()
            if st:
                lo = val - (i - st[-1] - 1)
                dp[i] = dp[st[-1]] + (lo + val) * (i - st[-1]) // 2
            elif val <= i + 1:
                dp[i] = (1 + val) * val // 2
            else:
                lo = val - i
                dp[i] = (lo + val) * (i + 1) // 2
            st.append(i)
            # print(st)
        # print(dp)
        return max(dp)