class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        sum = 0
        d = {0:1}
        for num in nums:
            sum += num
            # want to find ? = k, cur - ? = prev, so find cur - k = prev
            if sum - k in d:
                ans += d[sum - k]
            if sum in d: # add myself afterwards, otherwise cur - ? = cur gives empty []
                d[sum] += 1
            else:
                d[sum] = 1
        return ans