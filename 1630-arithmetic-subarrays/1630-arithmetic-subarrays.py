class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(nums)
        ans = []
        for a, b in zip(l, r):
            cur = sorted(nums[a:b+1])
            diff = cur[1] - cur[0]
            flag = True
            for i in range(2, len(cur)):
                if cur[i] - cur[i-1] != diff:
                    flag = False
                    break
            ans.append(flag)
        return ans