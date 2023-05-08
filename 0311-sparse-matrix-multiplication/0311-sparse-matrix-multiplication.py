class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])
        ans = [[0] * n for _ in range(m)]
        # naive
        for i in range(m):
            for j in range(n):
                for k_ in range(k):
                    ans[i][j] += mat1[i][k_] * mat2[k_][j]
        return ans