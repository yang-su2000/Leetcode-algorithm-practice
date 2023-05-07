class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ls = [0] # min-h at len-i
        ans = []
        for o in obstacles:
            i = bisect.bisect_right(ls, o)
            # print(o, i, ls)
            ans.append(i)
            if i == len(ls):
                ls.append(o)
            else:
                ls[i] = min(ls[i], o)
        return ans