class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        cur1 = 2**31
        cur2 = 2**31
        min2 = 2**31
        for i in nums:
            if i > min2:
                return True
            elif i < cur1:
                min2 = min(min2, cur2)
                cur1 = i
                cur2 = 2**31
            elif cur1 < i < cur2:
                cur2 = i
                min2 = min(min2, cur2)
        return False