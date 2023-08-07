class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m, n = len(mat), len(mat[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2
            val = mat[mid // n][mid % n]
            if val == target:
                return True
            elif val > target:
                r = mid - 1
            else:
                l = mid + 1
        return False