class Solution:
    def winnerOfGame(self, ls: str) -> bool:
        n = len(ls)
        a = 0
        b = 0
        for i in range(n):
            if i == 0 or i == n-1:
                continue
            if ls[i-1] != ls[i] or ls[i] != ls[i+1]:
                continue
            if ls[i] == 'A':
                a += 1
            else:
                b += 1
        return a > b