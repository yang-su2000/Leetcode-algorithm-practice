class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = Counter()
        for win, lose in matches:
            d[lose] += 1
            if win not in d:
                d[win] = 0
        ans = [[], []]
        for lose, count in d.items():
            if count <= 1:
                ans[count].append(lose)
        ans[0].sort()
        ans[1].sort()
        return ans