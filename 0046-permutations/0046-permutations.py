class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.dfs(nums, [False] * len(nums), [])
        return self.ans
    
    def dfs(self, nums, taken, ls):
        all_taken = True
        for i in range(len(nums)):
            if not taken[i]:
                all_taken = False
                taken[i] = True
                ls.append(nums[i])
                self.dfs(nums, taken, ls)
                ls.pop()
                taken[i] = False
        if all_taken:
            self.ans.append(ls.copy())