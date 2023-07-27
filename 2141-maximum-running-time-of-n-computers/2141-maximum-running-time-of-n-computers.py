class Solution:
    def maxRunTime(self, n: int, bat: List[int]) -> int:
        m = len(bat)
        l = 1
        r = sum(bat) // n
        bat.sort(reverse=True)
        while l < r:
            mid = (l + r) // 2 + 1
            count = sum(min(b, mid) for b in bat)
            if count >= n * mid:
                l = mid
            else:
                r = mid - 1
        return l