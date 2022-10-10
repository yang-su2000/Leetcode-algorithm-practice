class Solution:
    def breakPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return ''
        for i in range(len(s) // 2):
            if s[i] == 'a':
                continue
            return s[:i] + 'a' + s[i+1:]
        return s[:-1] + 'b'