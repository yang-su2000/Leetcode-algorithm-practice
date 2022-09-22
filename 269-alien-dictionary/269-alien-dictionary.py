class Solution:
    def add_rule(self, pre, cur):
        i, j = 0, 0
        n, m = len(pre), len(cur)
        while i < n and j < m:
            if pre[i] == cur[j]:
                i += 1
                j += 1
            else:
                self.rules[pre[i]].add(cur[j])
                return
        if n > m:
            self.invalid = True
    
    def add_child(self, parent, childs):
        s = set()
        while childs:
            c = childs.pop()
            if c not in s:
                s.add(c)
                if c in self.rules:
                    for c2 in self.rules[c]:
                        if c2 not in s:
                            childs.append(c2)
        self.childs[parent] = s
    
    def alienOrder(self, words: List[str]) -> str:
        A = defaultdict(set) # parent -> set(child)
        in_deg = defaultdict(int)
        for word in words:
            for c in word:
                in_deg[c] = 0
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
                        
                