class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        i, j = toBeRemoved[0], toBeRemoved[1]
        for a, b in intervals:
            if b <= i:
                ans.append([a, b])
            elif a < i:
                ans.append([a, i])
                if j < b:
                    ans.append([j, b])
            else:
                if j <= a:
                    ans.append([a, b])
                elif j < b:
                    ans.append([j, b])
        return ans