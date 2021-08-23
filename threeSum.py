class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if nums[i] > 0: # later two numbers are higher, break loop
                break
            if i == 0 or nums[i-1] != nums[i]: # remove duplicates of nums[i]
                self.twoSum(nums, i, res) # binary search by 2 pointers
        return res
    
    def twoSum(self, nums, i, res):
        n = len(nums)
        lo = i+1 # 2nd num
        hi = n-1 # 3rd num
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0 or (lo > i+1 and nums[lo] == nums[lo-1]): # remove duplicates of lo
                lo += 1 # hi goes from high to low, can only add lo
            elif sum > 0 or (hi < n-1 and nums[hi] == nums[hi+1]): # remove duplicates of hi
                hi -= 1 # lo goes from low to high, can only add hi
            else:
                res.append([nums[i], nums[lo], nums[hi]]) # reached target, add to result
                lo += 1 # and remove duplicates by updating lo and hi
                hi -= 1