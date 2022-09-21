class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        ans = [None] * n
        csum = sum([num for num in nums if num % 2 == 0])
        for i, [val, j] in enumerate(queries):
            if nums[j] % 2 == 0:
                csum -= nums[j]
            nums[j] += val
            if nums[j] % 2 == 0:
                csum += nums[j]
            ans[i] = csum
        return ans