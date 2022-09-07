class Solution:
    def merge(self, ls: List[List[int]]) -> List[List[int]]:
        ls.sort()
        ans = [ls[0]]
        for i in range(1, len(ls)):
            if ls[i][0] > ans[-1][1]:
                ans.append(ls[i])
            else:
                ans[-1][1] = max(ans[-1][1], ls[i][1])
        return ans