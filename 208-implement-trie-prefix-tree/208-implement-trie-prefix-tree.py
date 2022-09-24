class Trie:

    def __init__(self):
        self.val = False
        self.has_child = False
        self.children = [None] * 26

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                cur.children[i] = Trie()
            cur.has_child = True
            cur = cur.children[i]
        cur.val = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                return False
            cur = cur.children[i]
        return cur.val

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                return False
            cur = cur.children[i]
        return cur.val or cur.has_child


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)