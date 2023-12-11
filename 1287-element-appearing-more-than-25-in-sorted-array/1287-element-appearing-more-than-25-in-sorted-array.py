class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return sorted(Counter(arr).items(), key=lambda x: x[1])[-1][0]