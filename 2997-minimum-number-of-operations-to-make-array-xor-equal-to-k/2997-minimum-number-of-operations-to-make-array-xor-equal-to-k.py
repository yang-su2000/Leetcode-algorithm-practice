class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        val = k
        for i in nums:
            val ^= i
        return sum(1 for c in str(bin(val))[2:] if c == '1')