class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = set()
        prev_sum = nums[0] % k
        for i in nums[1:]:
            cur_sum = (prev_sum + i) % k
            if cur_sum in s or cur_sum == 0:
                return True
            s.add(prev_sum)
            prev_sum = cur_sum
        return False
            