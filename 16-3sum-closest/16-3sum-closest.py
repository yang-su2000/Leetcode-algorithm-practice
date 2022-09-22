class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = 10**5
        n = len(nums)
        ans = None
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                if abs(val - target) < diff:
                    diff = abs(val - target)
                    ans = val
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                if val < target:
                    j += 1
                elif val > target:
                    k -= 1
                else:
                    return ans
        return ans
            