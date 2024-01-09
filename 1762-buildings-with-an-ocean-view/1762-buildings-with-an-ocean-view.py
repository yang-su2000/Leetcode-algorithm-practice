class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = []
        for i in range(n):
            while ans and heights[ans[-1]] <= heights[i]:
                ans.pop()
            ans.append(i)
        return ans