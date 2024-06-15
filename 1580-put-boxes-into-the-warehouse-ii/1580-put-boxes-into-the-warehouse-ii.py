class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        ans = 0
        l = 0
        r = len(warehouse) - 1
        for b in sorted(boxes, reverse=True):
            if warehouse[l] < warehouse[r]:
                if b <= warehouse[r]:
                    ans += 1
                    r -= 1
            else:
                if b <= warehouse[l]:
                    ans += 1
                    l += 1
            if l > r:
                break
        return ans