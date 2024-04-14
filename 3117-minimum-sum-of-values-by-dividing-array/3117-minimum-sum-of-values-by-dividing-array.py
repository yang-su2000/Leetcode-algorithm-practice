class Solution:
    def minimumValueSum(self, nums: List[int], ands: List[int]) -> int:
        n = len(nums)
        m = len(ands)
        limit = -1
        dp = defaultdict(lambda: defaultdict(lambda: inf)) # m -> cval -> sval
        dp[0][limit] = 0
        for val in nums:
            dp2 = defaultdict(lambda: defaultdict(lambda: inf))
            for m_, d in dp.items():
                if m_ >= m:
                    continue
                for cval, mval in d.items():
                    cval2 = cval & val
                    if cval2 == ands[m_]:
                        dp2[m_ + 1][limit] = min(dp2[m_ + 1][limit], mval + val)
                    valid = True
                    for b in range(20):
                        if ((cval2 >> b) & 1) or (not ((ands[m_] >> b) & 1)):
                            pass
                        else:
                            valid = False
                            break
                    if valid:
                        dp2[m_][cval2] = min(dp2[m_][cval2], mval)
            dp = dp2
            # print(val)
            # for m_, d in dp.items():
            #     print(m_, "->", end=" ")
            #     for cval, mval in d.items():
            #         print(f"[{bin(cval)}, {mval}]", end=" ")
            #     print()
        return -1 if dp[m][limit] == inf else dp[m][limit]
        
        