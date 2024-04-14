class Solution:
    def minimumValueSum(self, nums: List[int], ands: List[int]) -> int:
        n = len(nums)
        m = len(ands)
        limit = -1
        
        @cache
        def dp(idx, m_, val):
            if idx == n:
                return 0 if m_ == m else inf
            if m_ == m:
                return inf
            val2 = val & nums[idx]
            ret = dp(idx + 1, m_, val2)
            if val2 == ands[m_]:
                ret = min(ret, dp(idx + 1, m_ + 1, limit) + nums[idx])
            # print(idx, m_, val2, ":", ret)
            return ret
        
        ans = dp(0, 0, limit)
        return ans if ans != inf else -1
        
        