class Solution:
    def canPlaceFlowers(self, ls: List[int], n: int) -> bool:
        for i in range(len(ls)):
            if (not ls[i]) and (i == 0 or ls[i-1] == 0) and (i == len(ls) - 1 or ls[i+1] == 0):
                n -= 1
                ls[i] = 1
        return n <= 0