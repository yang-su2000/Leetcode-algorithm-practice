class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            mid = l + (r - l) // 2 + 1
            miss = nums[mid] - nums[0] - mid
            # print(mid, miss)
            if miss > k:
                r = mid - 1
            elif miss == k:
                while mid and nums[mid - 1] + 1 == nums[mid]:
                    mid -= 1
                return nums[mid] - 1
            else:
                l = mid
        # print(l, r)
        return nums[l] + k - (nums[l] - nums[0] - l)