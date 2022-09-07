class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        for k in range(len(nums)):
            while i <= k <= j:
                if nums[k] == 0:
                    nums[i], nums[k] = nums[k], nums[i]
                    i += 1
                elif nums[k] == 1:
                    break
                else:
                    nums[j], nums[k] = nums[k], nums[j]
                    j -= 1
        return nums