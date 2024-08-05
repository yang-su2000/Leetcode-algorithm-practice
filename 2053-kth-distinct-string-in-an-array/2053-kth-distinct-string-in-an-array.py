class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        for s in arr:
            if c[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""