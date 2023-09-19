class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while 1:
            j = nums[i]
            if j < 0:
                return i
            nums[i] *= -1
            i = j