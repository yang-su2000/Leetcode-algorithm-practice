class Solution:
    def hammingWeight(self, n: int) -> int:
        return int.bit_count(n)