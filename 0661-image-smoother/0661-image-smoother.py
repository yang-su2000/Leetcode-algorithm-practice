class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        return [[sum(sum(row[max(0, j - 1): min(len(img[0]) - 1, j + 1) + 1]) for row in img[max(0, i - 1): min(len(img) - 1, i + 1) + 1]) // ((min(len(img) - 1, i + 1) - max(0, i - 1) + 1) * (min(len(img[0]) - 1, j + 1) - max(0, j - 1) + 1)) for j in range(len(img[0]))] for i in range(len(img))]