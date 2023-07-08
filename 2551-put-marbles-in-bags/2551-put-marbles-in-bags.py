class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1:
            return 0
        if n <= 2:
            return 0
        min_ = weights[0] + weights[-1]
        max_ = weights[0] + weights[-1]
        ls = [0] * (n - 1)
        for i in range(n - 1):
            ls[i] = weights[i] + weights[i+1]
        ls.sort()
        min_ += sum(ls[:k-1])
        max_ += sum(ls[-(k-1):])
        # print(ls)
        # print(max_, min_)
        return max_ - min_