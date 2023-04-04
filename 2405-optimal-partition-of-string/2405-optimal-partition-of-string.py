class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        d = set()
        for i in s:
            if i in d:
                d = set()
                count += 1
                d.add(i)
            else:
                d.add(i)
        return count