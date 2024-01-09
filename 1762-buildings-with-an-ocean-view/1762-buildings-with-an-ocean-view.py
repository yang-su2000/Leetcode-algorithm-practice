class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = []
        st = []
        for i in range(n-1, -1, -1):
            h = heights[i]
            while st and st[-1] < h:
                st.pop()
            if not st:
                ans.append(i)
            st.append(h)
        return reversed(ans)