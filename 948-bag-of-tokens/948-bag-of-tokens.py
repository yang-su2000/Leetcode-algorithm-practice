class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        q = deque(sorted(tokens))
        score = 0
        ans = 0
        while q:
            if power >= q[0]:
                power -= q.popleft()
                score += 1
                ans = max(ans, score)
            elif score > 0:
                power += q.pop()
                score -= 1
            else:
                break
        return ans