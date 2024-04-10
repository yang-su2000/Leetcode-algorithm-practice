class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        order = deque(range(n))
        order2 = []
        while order:
            order2.append(order.popleft())
            if order:
                order.append(order.popleft())
        ans = [0] * n
        for i in range(n):
            idx = order2[i]
            ans[idx] = deck[i]
        return ans