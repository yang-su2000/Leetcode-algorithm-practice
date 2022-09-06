class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ls = []
        for d1, n1 in enumerate(reversed(num1)):
            for d2, n2 in enumerate(reversed(num2)):
                if d1 + d2 == len(ls):
                    ls.append(0)
                ls[d1 + d2] += (ord(n1) - 48) * (ord(n2) - 48)
        i = 0
        while i < len(ls):
            if ls[i] >= 10:
                if i + 1 == len(ls):
                    ls.append(0)
                ls[i + 1] += ls[i] // 10
                ls[i] %= 10
            i += 1
        while len(ls) > 1 and ls[-1] == 0:
            ls.pop()
        ans = ''.join(reversed([chr(i + 48) for i in ls]))
        return ans