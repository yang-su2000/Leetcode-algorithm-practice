class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        d = deque()
        for i in arr:
            d.append(i)
            if len(d) > k:
                if abs(i - x) >= abs(d[0] - x):
                    d.pop()
                else:
                    d.popleft()
        return d