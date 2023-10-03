class Trie:

    def __init__(self):
        self.childs = {}
        self.count = 0

    def insert(self, word: str) -> None:
        t = self.locate(word, 0)
        t.count += 1

    def countWordsEqualTo(self, word: str) -> int:
        t = self.locate(word, 0)
        return t.count

    def countWordsStartingWith(self, prefix: str) -> int:
        t = self.locate(prefix, 0)
        return t.countSum()
        
    def countSum(self):
        ret = self.count
        for child in self.childs.values():
            ret += child.countSum()
        return ret

    def erase(self, word: str) -> None:
        t = self.locate(word, 0)
        t.count -= 1
    
    def locate(self, word, idx):
        if idx == len(word):
            return self
        c = word[idx]
        if c not in self.childs:
            self.childs[c] = Trie()
        return self.childs[c].locate(word, idx + 1)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)