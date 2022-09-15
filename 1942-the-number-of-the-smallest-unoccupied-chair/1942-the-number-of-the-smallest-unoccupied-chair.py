class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        max_chair = 0
        schedule = [] # pq: (time, leave=0 else 1, friend)
        n = len(times)
        for i in range(n):
            heapq.heappush(schedule, (times[i][0], 1, i))
            heapq.heappush(schedule, (times[i][1], 0, i))
        chairs = [] # current available chairs (any chair >= max_chair are available)
        records = {} # friend -> chair
        while schedule:
            time, is_arrive, friend = heapq.heappop(schedule)
            if is_arrive:
                if not chairs:
                    heapq.heappush(chairs, max_chair)
                    max_chair += 1
                chair = heapq.heappop(chairs)
                records[friend] = chair
                if friend == targetFriend:
                    return chair
            else:
                chair = records[friend]
                heapq.heappush(chairs, chair)
        return -1
            