class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        cur = [(-count, c) for c, count in Counter(s).items()]
        heapq.heapify(cur)
        while cur:
            count, c = heapq.heappop(cur)
            count = -count
            if ans and ans[-1] == c:
                if not cur:
                    return ""
                count2, c2 = heapq.heappop(cur)
                count2 = -count2
                ans.append(c2)
                count2 -= 1
                if count2:
                    heapq.heappush(cur, (-count2, c2))
            else:
                ans.append(c)
                count -= 1
            if count:
                heapq.heappush(cur, (-count, c))
        return ''.join(ans)
        