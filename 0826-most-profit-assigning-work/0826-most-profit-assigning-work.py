class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        diff_profit = []
        for diff, profit in sorted(zip(difficulty, profit)):
            if not diff_profit:
                diff_profit.append((diff, profit))
                continue
            if diff == diff_profit[-1][0]:
                diff_profit[-1] = (diff, max(diff_profit[-1][1], profit))
            elif profit <= diff_profit[-1][1]:
                continue
            else:
                diff_profit.append((diff, profit))
        ans = 0
        for w in worker:
            if diff_profit[0][0] > w:
                continue
            l = 0
            r = len(diff_profit) - 1
            while l < r:
                mid = (l + r + 1) // 2
                if diff_profit[mid][0] > w:
                    r = mid - 1
                else:
                    l = mid
            ans += diff_profit[l][1]
        return ans
        