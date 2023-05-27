class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        has0 = False
        pos = None
        neg = None
        for i in nums:
            if i > 0:
                pos, neg = pos * i if pos else i, neg * i if neg else None
            elif i < 0:
                pos, neg = \
                max(pos, neg * i if neg else i) if pos else (neg * i if neg else None), \
                min(neg, pos * i if pos else i) if neg else (pos * i if pos else i)
            else:
                has0 = True
            # print(pos, neg)
        if pos is not None:
            return pos
        if has0:
            return 0
        return neg