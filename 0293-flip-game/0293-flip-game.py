class Solution:
    def generatePossibleNextMoves(self, cur: str) -> List[str]:
        ans = []
        n = len(cur)
        for i in range(n - 1):
            if cur[i] == cur[i+1] == '+':
                ans.append(cur[:i] + '--' + cur[i+2:])
        return ans