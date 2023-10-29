class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        t = minutesToTest // minutesToDie + 1
        n = 0
        while t ** n < buckets:
            n += 1
        return n