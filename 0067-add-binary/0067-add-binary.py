class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry:
            cur = carry
            if i >= 0:
                if a[i] == '1': cur += 1
                i -= 1
            if j >= 0:
                if b[j] == '1': cur += 1
                j -= 1
            if cur == 0:
                ans += '0'
                carry = 0
            elif cur == 1:
                ans += '1'
                carry = 0
            elif cur == 2:
                ans += '0'
                carry = 1
            else:
                ans += '1'
                carry = 1
        return ans[::-1]