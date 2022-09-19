class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        target /= 2
        s = set()
        for i in nums:
            for j in list(s):
                if i + j <= target:
                    s.add(i + j)
            if i <= target:
                s.add(i)
            if target in s:
                return True
        return False