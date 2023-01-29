class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        flag = 0
        for i in piles:
            flag ^= i
        return flag