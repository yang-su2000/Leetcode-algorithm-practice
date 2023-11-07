class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        ls = []
        for d, s in zip(dist, speed):
            ls.append((d + s - 1) // s)
        ls.sort()
        # print(ls)
        n = len(ls)
        for i in range(n):
            if ls[i] < i + 1:
                return i
        return n