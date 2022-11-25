class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        st = []
        for i in range(n + 1):
            while st and (i == n or arr[st[-1]] >= arr[i]):
                cur = st.pop()
                l = -1 if not st else st[-1]
                r = i
                ans = (ans + arr[cur] * (cur-l) * (r-cur)) % (1e9+7)
            st.append(i)
        return int(ans)