class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        ans = 0
        n = len(img1)
        for a in range(-n, n):
            for b in range(-n, n):
                cur = 0
                for c in range(n):
                    for d in range(n):
                        if 0 <= c+a < n and 0 <= d+b < n and 1 == img1[c+a][d+b] == img2[c][d]:
                            cur += 1
                ans = max(ans, cur)
                # print(a, b, cur)
        return ans