class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        ans = 0
        A = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    A[i].append(j)
                    A[j].append(i)
        # print(A)
        full = (1 << n) - 1
        
        @cache
        def dfs(bit, i):
            nonlocal full, mod, A
            if bit == full:
                return 1
            ret = 0
            for j in A[i]:
                if (1 << j) & bit:
                    continue
                ret = (ret + dfs(bit | (1 << j), j)) % mod
            return ret
        
        ans = 0
        for i in range(n):
            ans = (ans + dfs(1 << i, i)) % mod
        return ans