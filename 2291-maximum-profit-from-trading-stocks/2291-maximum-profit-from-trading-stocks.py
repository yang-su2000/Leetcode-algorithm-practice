class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        n = len(present)
        d = {budget: 0}
        for p, f in zip(present, future):
            d2 = defaultdict(int)
            for balance, profit in d.items():
                if balance >= p:
                    d2[balance - p] = max(d2[balance - p], profit - p + f)
                d2[balance] = max(d2[balance], profit)
            d = d2
        return max(d.values())