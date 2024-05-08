class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        score = sorted([(score[i], i) for i in range(n)], reverse=True)
        ans = [None] * n
        for idx in range(n):
            val, i = score[idx]
            if idx == 0:
                ans[i] = 'Gold Medal'
            elif idx == 1:
                ans[i] = 'Silver Medal'
            elif idx == 2:
                ans[i] = 'Bronze Medal'
            else:
                ans[i] = str(idx + 1)
        return ans