class Solution:
    def intToRoman(self, num: int) -> str:
        d = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        i = 0
        ans = ''
        while i < len(d):
            if num // d[i][0]:
                ans += d[i][1]
                num -= d[i][0]
            else:
                i += 1
        return ans