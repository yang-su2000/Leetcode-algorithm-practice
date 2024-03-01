class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = -1
        for c in s:
            if c == '1':
                count += 1
        ans = '1' * count + '0' * (len(s) - count - 1) + '1'
        return ans