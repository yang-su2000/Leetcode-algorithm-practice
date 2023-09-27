class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        n = len(s)
        ls = [0] * n
        mult = [0] * n
        ls[0] = 1
        for i in range(n):
            if 'a' <= s[i] <= 'z':
                ls[i] = ls[i-1] + 1
            else:
                ls[i] = ls[i-1] * int(s[i])
                mult[i] = ls[i-1]
        # print(ls, mult)
        i = n - 1
        while k:
            if ls[i] == k and mult[i] == 0:
                return s[i]
            elif mult[i] == 0:
                if ls[i] < k:
                    k -= 1
            else:
                if mult[i] < k:
                    k %= mult[i]
                    if k == 0:
                        k += mult[i]
            i -= 1
            # print(i, ls[i], k)