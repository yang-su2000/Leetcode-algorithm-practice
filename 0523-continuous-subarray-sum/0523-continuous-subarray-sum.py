class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = set()
        prev = nums[0] % k
        for i in range(1, len(nums)):
            cur = (prev + nums[i]) % k
            if cur in s or cur == 0:
                return True
            s.add(prev)
            prev = cur
        # print(s)
        return False
            