class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def transform(i: int) -> int:
            return sum(int(c) for c in str(i))
        i = ''.join([str(ord(c) - ord('a') + 1) for c in s])
        while k:
            i = transform(i)
            k -= 1
        return i