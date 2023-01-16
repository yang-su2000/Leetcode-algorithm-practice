class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        left_ans = []
        right_ans = []
        for interval in intervals:
            # [right < new_left]
            if interval[1] < newInterval[0]:
                left_ans.append(interval)
            # [new_right < left]
            elif interval[0] > newInterval[1]:
                right_ans.append(interval)
            # [new_left <= right or left <= new_right]
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        return left_ans + [newInterval] + right_ans