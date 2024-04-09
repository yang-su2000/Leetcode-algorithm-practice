class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        val = tickets[k]
        ans = 0
        for i in range(len(tickets)):
            if i <= k:
                ans += min(val, tickets[i])
            else:
                ans += max(0, min(val - 1, tickets[i]))
        return ans