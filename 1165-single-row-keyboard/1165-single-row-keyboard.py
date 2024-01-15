class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {keyboard[i]: i for i in range(26)}
        return sum(abs(d[i] - d[j]) for i, j in pairwise(word)) + d[word[0]]