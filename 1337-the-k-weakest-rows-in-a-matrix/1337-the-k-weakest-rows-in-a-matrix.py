class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        vals = [] # (count, i)
        for i, row in enumerate(mat):
            count = sum(row)
            vals.append((count, i))
        vals.sort()
        return [i for _, i in vals][:k]