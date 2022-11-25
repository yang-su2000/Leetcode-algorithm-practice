class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        lo = [0] * n
        hi = [0] * n
        st = []
        for i in range(n):
            cur = 1
            while st and st[-1][0] > arr[i]:
                cur += st.pop()[1]
            st.append((arr[i], cur))
            lo[i] = cur
        st = []
        for i in range(n-1, -1, -1):
            cur = 1
            while st and st[-1][0] >= arr[i]:
                cur += st.pop()[1]
            st.append((arr[i], cur))
            hi[i] = cur
        ans = 0
        for i in range(n):
            # print(arr[i], lo[i], hi[i])
            ans = (ans + arr[i] * lo[i] * hi[i]) % (10**9+7)
        return int(ans)