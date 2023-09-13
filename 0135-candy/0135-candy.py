class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ls = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                ls[i] = ls[i-1] + 1
            else:
                ls[i] = 1
        # print(ls)
        for i in range(n):
            if not ((i == 0 or ratings[i-1] >= ratings[i]) and (i == n-1 or ratings[i] <= ratings[i+1])):
                continue
            l = i
            while l > 0 and ratings[l-1] > ratings[l]:
                ls[l-1] = max(ls[l-1], ls[l] + 1)
                l -= 1
            r = i
            while r < n - 1 and ratings[r] < ratings[r+1]:
                ls[r+1] = max(ls[r+1], ls[r] + 1)
                r += 1
        # print(ls)
        return sum(ls)