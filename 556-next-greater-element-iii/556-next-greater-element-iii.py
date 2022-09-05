class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = list(str(n))
        i = len(n) - 1
        while i >= 1 and n[i - 1] >= n[i]:
            i -= 1
        if i == 0:
            return -1
        n[i:] = sorted(n[i:])
        idx = i
        while n[idx] <= n[i-1]:
            idx += 1
        n[i-1], n[idx] = n[idx], n[i-1]
        n[i:] = sorted(n[i:])
        ans = int(''.join(n))
        if ans > 2**31-1:
            return -1
        return ans
        