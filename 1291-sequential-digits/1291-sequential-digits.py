class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = '123456789'
        ans = set()
        for l in range(9):
            for r in range(l, 10):
                val = int(s[l:r+1])
                if low <= val <= high:
                    ans.add(val)
        return sorted(ans)