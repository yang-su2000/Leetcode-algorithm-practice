class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ls = sorted(Counter(candidates).items())
        ans = []
        # print(ls)
        
        def bt(i, cur, val):
            if i == len(ls):
                if val == target:
                    ans.append(cur.copy())
                return
            for _ in range(ls[i][1] + 1):
                if val <= target:
                    bt(i + 1, cur, val)
                cur.append(ls[i][0])
                val += ls[i][0]
            for _ in range(ls[i][1] + 1):
                cur.pop()
                
        bt(0, [], 0)
        
        return ans