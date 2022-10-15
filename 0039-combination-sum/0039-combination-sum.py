class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = set()
        self.dfs(candidates, target, [])
        return [list(ls) for ls in self.ans]
    
    def dfs(self, can, remain, ls):
        if remain == 0:
            self.ans.add(tuple(sorted(ls)))
            return
        for i in can:
            if remain >= i:
                ls.append(i)
                self.dfs(can, remain - i, ls)
                ls.pop()