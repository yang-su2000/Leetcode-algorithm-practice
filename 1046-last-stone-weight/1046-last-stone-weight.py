import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)
        while len(stones) >= 2:
            i = heappop(stones)
            j = heappop(stones)
            # print(i, j)
            if i == j:
                continue
            else:
                heappush(stones, -abs(i-j))
        return 0 if not stones else -stones[0]