class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def bt(i, ls):
            if i == len(nums):
                ans.add(tuple(sorted(ls)))
                return
            bt(i+1, ls)
            ls.append(nums[i])
            bt(i+1, ls)
            ls.pop()
            
        bt(0, [])
        return [list(i) for i in ans]