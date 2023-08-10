class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def same_side(i):
            if nums[0] <= target and nums[0] <= nums[i]:
                return True
            if nums[0] > target and nums[0] > nums[i]:
                return True
            return False
        l = 0
        r = len(nums) - 1
        while l < r:
            while l < r and nums[l] == nums[l+1]:
                l += 1
            while l < r and nums[r] == nums[r-1]:
                r -= 1
            if l == r:
                break
            mid = l + (r - l) // 2
            val = None
            if same_side(mid):
                val = nums[mid]
            elif nums[0] <= target:
                val = inf
            else:
                val = -inf
            if val == target:
                return True
            elif val > target:
                r = mid - 1
            else:
                l = mid + 1
        return nums[l] == target