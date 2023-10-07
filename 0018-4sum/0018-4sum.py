class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = set()
        for i in range(n):
            seen = defaultdict(set) # sum2 -> (a, b)
            for l in range(i):
                for l2 in range(l + 1, i):
                    a, b = nums[l], nums[l2]
                    sum2 = a + b
                    seen[sum2].add((a, b))
            seen2 = defaultdict(set)
            for r in range(i, n):
                for r2 in range(r + 1, n):
                    c, d = nums[r], nums[r2]
                    sum2 = c + d
                    seen2[sum2].add((c, d))
            for v, sets in seen.items():
                if target - v in seen2:
                    sets2 = seen2[target - v]
                    for a, b in sets:
                        for c, d in sets2:
                            ans.add(tuple(sorted([a, b, c, d])))
        return [list(t) for t in ans]