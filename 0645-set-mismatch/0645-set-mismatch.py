class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        twice = 0
        d = Counter(nums)
        for k, v in d.items():
            if v == 2:
                twice = k
        miss = 0
        for i in range(1, len(nums) + 1):
            if i not in d:
                miss = i
        return [twice, miss]