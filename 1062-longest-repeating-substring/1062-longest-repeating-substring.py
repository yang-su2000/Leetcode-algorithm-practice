class Trie:
    ans = 0

    def __init__(self, depth):
        self.count = 0
        self.depth = depth
        self.child = {}
        
    def trace(self, s, i):
        if i == len(s):
            return
        if s[i] not in self.child:
            self.child[s[i]] = Trie(self.depth + 1)
        t = self.child[s[i]]
        if t.count:
            Trie.ans = max(Trie.ans, t.depth)
        t.count += 1
        t.trace(s, i + 1)
        

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        Trie.ans = 0
        T = Trie(0)
        for i in range(len(s)):
            T.trace(s, i)
        return Trie.ans