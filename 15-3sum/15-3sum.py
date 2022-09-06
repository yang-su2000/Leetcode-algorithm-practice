class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        d = defaultdict(lambda: 0) # num -> max index
        for i, num in enumerate(nums):
            d[num] = max(d[num], i)
        for i in range(len(nums)):
            ni = nums[i]
            for j in range(i + 1, len(nums)):
                nj = nums[j]
                target = -(ni + nj)
                if target in d and d[target] > j:
                    ans.add((ni, nj, target))
        return [list(t) for t in list(ans)]
                    