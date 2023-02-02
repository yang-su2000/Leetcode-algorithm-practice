class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = string.ascii_lowercase
        d = {order[i]: alphabet[i] for i in range(len(order))}
        words2 = []
        for word in words:
            word2 = ''.join([d[c] for c in word])
            words2.append(word2)
        return sorted(words2) == words2
            