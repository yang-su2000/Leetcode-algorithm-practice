class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        cmax = max(candies)
        return [i + extraCandies >= cmax for i in candies]