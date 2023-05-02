class Solution:
    def arraySign(self, nums: List[int]) -> int:
        pos = True
        for i in nums:
            if not i:
                return 0
            if i < 0:
                pos = not pos
        return 1 if pos else -1