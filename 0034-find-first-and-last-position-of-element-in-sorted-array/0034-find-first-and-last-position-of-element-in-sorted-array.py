class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        p = self.search(nums, target)
        # print(p)
        if p == -1:
            return [-1, -1]
        l = self.search_left(nums, target, 0, p)
        r = self.search_right(nums, target, p, len(nums) - 1)
        return [l, r]
    
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if l == len(nums) or nums[l] != target:
            return -1
        return l
    
    def search_left(self, nums, target, l, r):
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                r = mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l
    
    def search_right(self, nums, target, l, r):
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] == target:
                l = mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l