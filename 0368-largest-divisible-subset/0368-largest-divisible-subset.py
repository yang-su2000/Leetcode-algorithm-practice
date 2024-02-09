class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        cand = [[] for _ in range(n)]
        ans = []
        for i in range(n):
            j2 = -1
            for j in range(i):
                if nums[i] % nums[j] == 0 and (len(cand[j]) > len(cand[j2]) or j2 == -1):
                    j2 = j
            if j2 != -1:
                cand[i] = cand[j2].copy()
            cand[i].append(nums[i])
            if len(cand[i]) > len(ans):
                ans = cand[i]
        return ans