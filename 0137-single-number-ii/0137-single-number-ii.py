class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in nums:
            a = (~b) & (a ^ i)
            b = (~a) & (b ^ i)
            # print(i, a, b)
        return a