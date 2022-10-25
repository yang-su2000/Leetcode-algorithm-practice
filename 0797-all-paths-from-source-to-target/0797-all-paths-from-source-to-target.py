class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        
        def bt(s):
            nonlocal ans
            if s[-1] == len(graph) - 1:
                ans.append(s.copy())
                return
            cur = graph[s[-1]]
            if not cur:
                return
            for i in cur:
                s.append(i)
                bt(s)
                s.pop()
            
        bt([0])
        return ans