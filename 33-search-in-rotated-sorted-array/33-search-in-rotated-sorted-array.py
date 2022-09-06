class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        hi_flag = (target >= nums[0])
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            cur_flag = (nums[mid] >= nums[0])
            if nums[mid] > target:
                if cur_flag == hi_flag:
                    r = mid - 1
                elif hi_flag:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if cur_flag == hi_flag:
                    l = mid + 1
                elif hi_flag:
                    r = mid - 1
                else:
                    l = mid + 1
        return l if nums[l] == target else -1