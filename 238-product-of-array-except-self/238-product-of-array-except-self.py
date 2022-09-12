class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pres = [0] * n
        sufs = [0] * n
        pres[0] = nums[0]
        sufs[-1] = nums[-1]
        for i in range(1, n):
            pres[i] = pres[i-1] * nums[i]
        for i in range(n-2, -1, -1):
            sufs[i] = sufs[i+1] * nums[i]
        print(pres, sufs)
        ans = [0] * n
        for i in range(n):
            l = pres[i-1] if i else 1
            r = sufs[i+1] if i + 1 < n else 1
            ans[i] = l * r
        return ans