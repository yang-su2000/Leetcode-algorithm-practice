class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                # Mark the node as end of a prefix
                node.is_end = True

        n = len(target)
        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == sys.maxsize:
                continue
            node = root
            j = i
            while j < n and target[j] in node.children:
                node = node.children[target[j]]
                j += 1
                if node.is_end:
                    if dp[j] > dp[i] + 1:
                        dp[j] = dp[i] + 1

        return dp[n] if dp[n] != sys.maxsize else -1
