class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        cur = 10**9+1
        for num in nums:
            if num == cur:
                count += 1
            else:
                count -= 1
                if count == 0:
                    count += 1
                    cur = num
        return cur