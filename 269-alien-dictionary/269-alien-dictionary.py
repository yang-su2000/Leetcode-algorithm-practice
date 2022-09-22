class Solution:
    def alienOrder(self, words: List[str]) -> str:
        A = defaultdict(set) # parent -> set(child)
        in_deg = defaultdict(int)
        for word in words:
            for c in word:
                in_deg[c] = 0
        # create A and in_deg
        for i in range(1, len(words)):
            done = False
            for c1, c2 in zip(words[i-1], words[i]):
                if c1 != c2:
                    done = True
                    if c2 not in A[c1]:
                        A[c1].add(c2)
                        in_deg[c2] += 1
                    break
            if not done and len(words[i-1]) > len(words[i]):
                    return ''
        # topological sort
        ans = []
        q = deque([c for c in in_deg if in_deg[c] == 0])
        while q:
            c1 = q.popleft()
            ans.append(c1)
            for c2 in A[c1]:
                in_deg[c2] -= 1
                if in_deg[c2] == 0:
                    q.append(c2)
        if len(ans) != len(in_deg):
            return ''
        return ''.join(ans)
                        
                