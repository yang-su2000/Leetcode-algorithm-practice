class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            gl = (mid == 0 or nums[mid - 1] < nums[mid]) # greater than left
            gr = (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]) # greater than right
            if gl and gr:
                return mid
            elif gl:
                l = mid + 1
            else:
                r = mid - 1
        return -1
                
                