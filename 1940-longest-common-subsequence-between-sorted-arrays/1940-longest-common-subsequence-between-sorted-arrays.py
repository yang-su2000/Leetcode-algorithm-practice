class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        ans = []
        cur = 1
        n = len(arrays)
        idxs = [0] * n
        while cur <= 100:
            valid = True
            for i in range(n):
                if idxs[i] < len(arrays[i]) and arrays[i][idxs[i]] == cur:
                    idxs[i] += 1
                else:
                    valid = False
            if valid:
                ans.append(cur)
            cur += 1
        return ans