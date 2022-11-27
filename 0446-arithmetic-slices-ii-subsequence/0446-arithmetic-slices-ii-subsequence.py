class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        ans = 0
        dp = [defaultdict(int) for _ in range(n)] # r: (add -> count)
        for r in range(1, n):
            rval = nums[r]
            for l in range(r):
                lval = nums[l]
                add = rval - lval
                csum = 0
                if add in dp[l]:
                    csum = dp[l][add]
                dp[r][add] += csum + 1
                ans += csum
            # print(dp[r].items())
        return ans
        
        # d1 = defaultdict(set) # rval -> (r)
        # d2 = [defaultdict(int) for _ in range(n)] # r: (add -> count)
        # ans = 0
        # for r in range(1, n):
        #     rval = nums[r]
        #     for l in range(r):
        #         lval = nums[l]
        #         add = rval - lval
        #         if rval in d1:
        #             s = d1[rval]
        #             for prev_r in s:
        #                 d = d2[prev_r]
        #                 if add in d:
        #                     d1
        #                     count = d.pop(add)
        #                     d1[rval + add].add(r)
        #                     d2[r][add] = count + 1
        #                     ans += max(0, count - 1)
                            
                # if p in d:
                #     d2 = d[p]
                #     for prev_r, prev_count in d2:
                #         count, _ = d.pop(p)
                #         d[(rval + add, add)] = (count + 1, r)
                #         ans += max(0, count - 1)
                # else:
                #     d[(rval + add, add)] = (2, r)
        return ans