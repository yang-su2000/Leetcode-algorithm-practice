class Solution:
    def findOrder(self, numCourses: int, pres: List[List[int]]) -> List[int]:
        afters = [[] for _ in range(numCourses)]
        counts = [0 for _ in range(numCourses)]
        for p in pres:
            afters[p[1]].append(p[0])
            counts[p[0]] += 1
        # print(afters)
        # print(counts)
        stack = []
        ans = []
        for i in range(numCourses):
            if counts[i] == 0:
                stack.append(i)
                ans.append(i)
        while stack:
            i = stack.pop()
            for j in afters[i]:
                counts[j] -= 1
                if counts[j] == 0:
                    stack.append(j)
                    ans.append(j)
        if len(ans) != numCourses:
            return []
        return ans