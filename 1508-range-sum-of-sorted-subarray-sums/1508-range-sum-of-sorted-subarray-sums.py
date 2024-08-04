class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ls = []
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + sums[-1])
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                ls.append(sums[j] - (sums[i-1] if i else 0))
        return sum(sorted(ls)[left-1: right]) % int(1e9+7)