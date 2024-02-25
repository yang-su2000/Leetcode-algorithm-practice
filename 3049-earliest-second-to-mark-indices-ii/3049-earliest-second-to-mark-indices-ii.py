class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n = len(nums)
        m = len(changeIndices)
        first = [-1] * n
        for i in range(m-1, -1, -1):
            idx = changeIndices[i] - 1
            first[idx] = i
        
        def solve(bound):
            cur = 0 # store index used to do normal decrement or mark
            mark = [False] * n
            pq = [] # (nums[i], idx)
            for i in range(bound, -1, -1):
                idx = changeIndices[i] - 1
                val = nums[idx]
                if val <= 1 or first[idx] != i:
                    cur += 1
                    continue
                if cur < 1: # cannot use idx to mark (which uses 1 cur)
                    if (not pq) or val <= pq[0][0]: # val is beter to not use idx because it is lowest
                        cur += 1
                        continue
                    else: # val is better to use idx, regret previous best val2
                        val2, idx2 = heappop(pq)
                        cur += 1 # because idx2 can now be used normally
                        heappush(pq, (val, idx))
                        mark[idx2] = False
                        cur += 1 # regret 1 index used to mark idx2
                        mark[idx] = True
                        cur -= 1 # mark idx costs 1
                else:
                    heappush(pq, (val, idx))
                    mark[idx] = True
                    cur -= 1
            for i in range(n):
                if not mark[i]:
                    cur -= nums[i] + 1 # cost nums[idx] to decrement to 0, then mark costs 1
            return cur >= 0
                
        l = 0
        r = m - 1
        if not solve(r):
            return -1
        while l < r:
            mid = (l + r) // 2
            if solve(mid):
                r = mid
            else:
                l = mid + 1
        return l + 1