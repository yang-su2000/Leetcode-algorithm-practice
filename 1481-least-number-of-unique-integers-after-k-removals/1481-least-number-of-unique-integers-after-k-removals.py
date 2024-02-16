class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        ls = list(sorted(Counter(arr).values()))
        # print(ls)
        n = len(ls)
        for i in range(n):
            if k < ls[i]:
                return n - i
            elif k == ls[i]:
                return n - i - 1
            k -= ls[i]
        return 0