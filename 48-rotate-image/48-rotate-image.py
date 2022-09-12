class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(m)
        # 0,0 | 0,n-1 | n-1,n-1 | n-1,0
        # 0,1 | 1,n-1 | n-1,n-1-1 | n-1-1,0
        # ...
        # ...
        # 1,1 | 1,n-2 | n-2,n-2 | n-2,1
        for i in range(n//2):
            i2 = n-i-1
            for j in range(i, n-i-1):
                j2 = n-j-1
                # print(i, i2, j, j2)
                # print(m[i][j], m[j][i2], m[i2][j2], m[j2][i])
                m[i][j], m[j][i2], m[i2][j2], m[j2][i] = m[j2][i], m[i][j], m[j][i2], m[i2][j2]