class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not n:
            return len(tasks)
        # priority (lowest wait time, highest remaining tasks count)
        d = defaultdict(lambda: 0)
        for t in tasks:
            d[t] += 1
        pq = []
        for k, v in d.items():
            heapq.heappush(pq, (0, -v))
        ans = 0
        while pq:
            # print(pq)
            time, count = heapq.heappop(pq)
            ans += time + 1
            for i in range(len(pq)):
                pq[i] = (max(0, pq[i][0] - time - 1), pq[i][1])
            if count + 1 != 0:
                pq.append((n, count + 1))
            heapq.heapify(pq)
        return ans