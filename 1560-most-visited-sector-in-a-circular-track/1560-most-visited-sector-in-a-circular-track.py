class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        count = [0] * n
        m = len(rounds)
        for i in range(1, m):
            j = rounds[i-1] - 1
            j2 = rounds[i] - 1
            while j != j2:
                count[j] += 1
                j = (j + 1) % n
        count[rounds[-1] - 1] += 1
        maxi = max(count)
        return [i + 1 for i in range(n) if count[i] == maxi]