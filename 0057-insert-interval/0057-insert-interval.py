class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        ans = []
        is_inserted = False
        for interval in intervals:
            if is_inserted:
                ans.append(interval)
            # [left <= right < new_left]
            elif interval[1] < newInterval[0]:
                ans.append(interval)
            # [left <= new_right or right]
            elif interval[0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            # [new_right < left]
            else:
                is_inserted = True
                ans.append(newInterval)
                ans.append(interval)
            # print(ans, newInterval)
        if not is_inserted:
            ans.append(newInterval)
        return ans