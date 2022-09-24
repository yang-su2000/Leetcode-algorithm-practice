class Solution:
    def calculate(self, s: str) -> int:
        ls = [0]
        symbol = set(['+','-','*','/'])
        for i in s:
            if i == ' ':
                continue
            elif i in symbol:
                ls.append(i)
            elif type(ls[-1]) is int:
                ls[-1] = ls[-1] * 10 + int(i)
            else:
                ls.append(int(i))
        print(ls)
        ls2 = []
        prior = set(['*','/'])
        for i in ls:
            if type(i) is int:
                if ls2 and ls2[-1] in prior:
                    sym = ls2.pop()
                    i0 = ls2.pop()
                    if sym == '*':
                        i0 *= i
                    else:
                        i0 //= i
                    ls2.append(i0)
                else:
                    ls2.append(i)
            else:
                ls2.append(i)
        print(ls2)
        ans = ls2[0]
        for i in range(1, len(ls2), 2):
            if ls2[i] == '+':
                ans += ls2[i+1]
            else:
                ans -= ls2[i+1]
        return ans
                    