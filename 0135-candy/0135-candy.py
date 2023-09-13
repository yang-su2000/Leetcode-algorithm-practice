class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        l, r = [1] * n, [1] * n
        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                l[i] = l[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                r[i] = r[i+1] + 1
        return sum(max(a, b) for a, b in zip(l, r))