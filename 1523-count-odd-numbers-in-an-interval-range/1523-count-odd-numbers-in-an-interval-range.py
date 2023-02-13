class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return high // 2 + high % 2 - (low - 1) // 2 - (low - 1) % 2