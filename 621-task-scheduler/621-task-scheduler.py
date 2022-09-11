class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for t in tasks:
            counts[ord(t) - ord('A')] += 1
        counts.sort()
        max_count = counts.pop()
        idle = (max_count - 1) * n
        while counts and idle > 0:
            idle -= min(max_count - 1, counts.pop())
        return max(0, idle) + len(tasks)