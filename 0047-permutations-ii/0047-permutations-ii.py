class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        d = Counter(nums)
        
        def bt(cur):
            if len(cur) == n:
                ans.append(cur.copy())
                return
            for key in d.keys():
                if d[key]:
                    d[key] -= 1
                    cur.append(key)
                    bt(cur)
                    d[key] += 1
                    cur.pop()
        
        bt([])
        return ans