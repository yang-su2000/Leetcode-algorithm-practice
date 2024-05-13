class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        ls = []
        for i in range(n):
            for j in range(i + 1, n):
                ls.append((arr[i] / arr[j], arr[i], arr[j]))
        ls.sort()
        # print(ls)
        return [ls[k-1][1], ls[k-1][2]]