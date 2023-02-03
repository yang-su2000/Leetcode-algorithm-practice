class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        pivot = 2 * numRows - 2
        ans = ['' for _ in range(numRows)]
        for i, c in enumerate(s):
            p = i % pivot
            if p >= numRows:
                p = pivot - p
            ans[p] += c
        return ''.join(ans)