class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0
        if left:
            ans = max(ans, max(left))
        if right:
            ans = max(ans, n - min(right))
        return ans
        # left.sort()
        # right.sort()
        # ans = 0
        # for i in right:
        #     p = bisect_left(left, i)
        #     if p < len(left):
        #         ans = max(ans, left[p])
        #     else:
        #         ans = max(ans, n - i)
        #     print("r", i, p)
        # for i in left:
        #     p = bisect_left(right, i) - 1
        #     if p >= 0:
        #         ans = max(ans, n - right[p])
        #     else:
        #         ans = max(ans, i)
        #     print("l", i, p)
        # return ans