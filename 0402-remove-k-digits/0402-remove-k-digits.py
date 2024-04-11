class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ls = []
        for c in num:
            while k and ls and ls[-1] > c:
                k -= 1
                ls.pop()
            ls.append(c)
        while k:
            k -= 1
            ls.pop()
        num = ''.join(ls)
        for i in range(len(num)):
            if num[i] != '0':
                return num[i:]
        return '0'