class Union:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def link(self, x, y):
        x, y = self.find(x), self.find(y)
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.size[x] += self.size[y]
        self.p[y] = x

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ls = sorted(((nums[i], i) for i in range(n)), reverse=True)
        U = Union(n)
        vis = [False] * n
        ans = 0
        for _, i in ls:
            if i < n-1 and vis[i+1]:
                U.link(i, i+1)
            ans += U.size[U.p[i]]
            if 0 < i and vis[i-1]:
                U.link(i-1, i)
            vis[i] = True
        return ans