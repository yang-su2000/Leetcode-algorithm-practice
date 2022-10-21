class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i, x in enumerate(nums):
            if x in s:
                return True
            s.add(x)
            if len(s) > k:
                s.remove(nums[i-k])
        return False