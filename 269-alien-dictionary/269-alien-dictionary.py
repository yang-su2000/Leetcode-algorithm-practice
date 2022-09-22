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
        self.rules = defaultdict(set) # parent -> child
        self.invalid = False
        for i in range(1, len(words)):
            self.add_rule(words[i-1], words[i])
        if self.invalid:
            return ''
        for word in words:
            for c in word:
                if c not in self.rules:
                    self.rules[c] = set()
        print(self.rules.items())
        self.childs = defaultdict(set)
        for parent, childs in self.rules.items():
            self.add_child(parent, list(childs))
        print(self.childs.items())
        ans = []
        while self.childs:
            cur = []
            childs2 = defaultdict(set)
            for parent, childs in self.childs.items():
                if not childs:
                    cur.append(parent)
                else:
                    childs2[parent] = childs
            if not cur:
                return ''
            for parent, childs in childs2.items():
                for c in cur:
                    if c in childs:
                         childs.remove(c)
            self.childs = childs2
            print(cur)
            ans.extend(cur)
        return ''.join(ans[::-1])
                