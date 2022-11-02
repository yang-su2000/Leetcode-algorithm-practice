class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        commons = set(mat[0])
        for i in range(1, len(mat)):
            commons &= set(mat[i])
        if not commons:
            return -1
        counter = Counter()
        for row in mat:
            counter += Counter(row)
        d = {}
        for i in commons:
            d[i] = counter[i]
        ans = list(d.items())
        ans.sort(key=lambda t:t[1])
        return ans[0][0]