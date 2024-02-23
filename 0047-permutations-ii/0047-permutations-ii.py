class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        
        def bt(cur, taken, count):
            if count == n:
                ans.add(tuple(cur))
                return
            for i in range(n):
                if not taken[i]:
                    taken[i] = True
                    cur.append(nums[i])
                    bt(cur, taken, count + 1)
                    taken[i] = False
                    cur.pop()
        
        bt([], [False] * n, 0)
        ans = [list(t) for t in ans]
        return ans