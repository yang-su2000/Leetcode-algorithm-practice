class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev = 0
        cur = 0
        ans = 0
        flip = False
        for i in nums:
            if i == 1:
                cur += 1
            elif not flip:
                flip = True
                prev = cur
                cur = 0
            else:
                # print(prev + cur)
                ans = max(ans, prev + cur + 1)
                prev = cur
                cur = 0
        # print(prev + cur)
        ans = max(ans, prev + cur + (1 if flip else 0))
        return ans