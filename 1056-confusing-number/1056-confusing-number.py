class Solution:
    def confusingNumber(self, n: int) -> bool:
        if set(str(n)) & {'2', '3', '4', '5', '7'}:
            return False
        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        s = ''
        for i in str(n):
            s += d[i]
        return s[::-1] != str(n)