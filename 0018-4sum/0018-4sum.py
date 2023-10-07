class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        def kSum(nums, target, k):
            if k == 2:
                ret = []
                l = 0
                r = len(nums) - 1
                while l < r:
                    csum = nums[l] + nums[r]
                    if csum < target or (l > 0 and nums[l] == nums[l-1]):
                        l += 1
                    elif csum > target or (r < len(nums)-1 and nums[r] == nums[r+1]):
                        r -= 1
                    else:
                        ret.append([nums[l], nums[r]])
                        l += 1
                        r -= 1
                return ret
            ret = []
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i-1]:
                    for cur in kSum(nums[i+1:], target - nums[i], k - 1):
                        ret.append([nums[i]] + cur)
            return ret
        return kSum(nums, target, 4)