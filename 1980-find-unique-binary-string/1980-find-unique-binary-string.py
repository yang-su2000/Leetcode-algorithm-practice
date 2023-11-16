class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        s = set(nums)
        for i in range(1 << n):
            val = ''.join('1' if i >> b & 1 else '0' for b in range(n))
            if val not in s:
                return val