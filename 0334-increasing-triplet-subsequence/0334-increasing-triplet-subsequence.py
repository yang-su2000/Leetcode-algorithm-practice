class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        cur1 = float('Inf')
        cur2 = float('Inf')
        for i in nums:
            if i <= cur1:
                cur1 = i
            elif i <= cur2:
                cur2 = i
            else:
                return True
        return False