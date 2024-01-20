class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        s = []
        for i in range(n):
            while s and i + k - len(s) < n and nums[s[-1]] > nums[i]:
                s.pop()
            s.append(i)
        return [nums[i] for i in s[:k]]