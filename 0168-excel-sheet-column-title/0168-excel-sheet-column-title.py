class Solution:
    def convertToTitle(self, i: int) -> str:
        ans = []
        while i >= 1:
            i -= 1
            ans.append(chr(i % 26 + ord('A')))
            i //= 26
        return ''.join(ans[::-1])