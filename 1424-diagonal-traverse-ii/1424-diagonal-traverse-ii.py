class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        idxs = [0] * n
        cur = [0]
        ans = []
        count = 0
        while cur:
            nxt = []
            count += 1
            if count < n:
                nxt.append(count)
            for row in cur:
                idx = idxs[row]
                ans.append(nums[row][idx])
                idxs[row] += 1
                if idxs[row] < len(nums[row]):
                    nxt.append(row)
            cur = nxt
        return ans