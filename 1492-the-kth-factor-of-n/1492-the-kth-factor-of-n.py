class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, n + 1):
            if n % i == 0:
                if k == 1:
                    return i
                k -= 1
        return -1