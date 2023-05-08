class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])
        ans = [[0] * n for _ in range(m)]
        
        # naive
        # for i in range(m):
        #     for j in range(n):
        #         for k_ in range(k):
        #             ans[i][j] += mat1[i][k_] * mat2[k_][j]
        # return ans
        
        # sklearn sparse
        d1 = {}
        for i in range(m):
            for j in range(k):
                if mat1[i][j]:
                    d1[(i, j)] = mat1[i][j]
        d2 = {}
        for i in range(k):
            for j in range(n):
                if mat2[i][j]:
                    d2[(i, j)] = mat2[i][j]
        for (i, j), val in d1.items():
            for (i2, j2), val2 in d2.items():
                if j == i2:
                    ans[i][j2] += val * val2
        return ans
        