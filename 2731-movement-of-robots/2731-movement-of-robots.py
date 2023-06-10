class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(nums)
        ls = [nums[i] + (-d if s[i] == 'L' else d) for i in range(n)]
        ls.sort()
        # print(ls)
        ans = 0
        psum = 0
        for i in range(1, n):
            psum += i * (ls[i] - ls[i-1])
            ans += psum
        return ans % int(1e9+7)