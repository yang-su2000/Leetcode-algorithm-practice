class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10**9+7
        
        def trace(ls):
            nonlocal mod
            if len(ls) < 3:
                return 1
            l = [i for i in ls if i < ls[0]]
            r = [i for i in ls if i > ls[0]]
            return (comb(len(ls) - 1, len(l)) * trace(l) * trace(r)) % mod
        
        ans = trace(nums)
        return (ans - 1) % mod