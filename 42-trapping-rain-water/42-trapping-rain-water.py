class Solution:
    def trap(self, ls: List[int]) -> int:
        n = len(ls)
        ans = 0
        left_h, left_sum = 0, 0
        for h in ls:
            if h >= left_h:
                ans += left_sum
                left_h, left_sum = h, 0
            else:
                left_sum += left_h - h
        right_h, right_sum = 0, 0
        for h in ls[::-1]:
            if h > right_h:
                ans += right_sum
                right_h, right_sum = h, 0
            else:
                right_sum += right_h -h
        return ans
            