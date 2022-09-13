class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        n1, n2 = len(num1), len(num2)
        add = 0
        ans = ''
        i = 0
        while i < n1 or i < n2 or add:
            cur = add
            add = 0
            if i < n1:
                cur += ord(num1[i]) - ord('0')
            if i < n2:
                cur += ord(num2[i]) - ord('0')
            if cur >= 10:
                cur -= 10
                add = 1
            ans += chr(cur + ord('0'))
            i += 1
        return ans[::-1]