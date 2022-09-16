class Solution:
    def maximumScore(self, nums: List[int], ms: List[int]) -> int:
        n = len(nums)
        m = len(ms)
        dp = [[0] * (m+1) for _ in range(m+1)]
        for op in range(m-1, -1, -1):
            for left in range(op, -1, -1):
                # op: num of operations needed to be done
                # left: num of left nums have used
                # current dp: max(a, b)
                # a: based on the previous score given the left index is actually used
                # which is (1 more operations needed, 1 right index given the current index l is actually used)
                
                # [side] right index calculation
                # num of right nums have used (right) = op - left
                # remaining nums (remain) = n - left - right
                # the right index = l + remain - 1 = (n-1) - (op-left)
                
                # b: based on the previous score given the right index is actually used
                # which is (1 more operations needed, no left index change given the rightmost index r is actually used)
                dp[op][left] = max(ms[op] * nums[left] + dp[op+1][left+1], \
                                   ms[op] * nums[(n-1) - (op-left)] + dp[op+1][left])
        # the base case is 0 operations needed (i.e. all used) and 0 left nums is used
        return dp[0][0]