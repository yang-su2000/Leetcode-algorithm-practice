class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0: return 0
        l = 0
        r = int(1e9)
        nums.sort()
        
        def solve(val):
            cp = 0
            i = 0
            n = len(nums)
            while i < n:
                if i < n - 1 and nums[i+1] - nums[i] <= val:
                    i += 2
                    cp += 1
                    if cp == p:
                        break
                else:
                    i += 1
            return cp == p
        
        while l < r:
            mid = (l + r) // 2
            if solve(mid):
                r = mid
            else:
                l = mid + 1
        return l