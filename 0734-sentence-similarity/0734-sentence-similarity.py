class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        d = defaultdict(lambda: set())
        for a, b in similarPairs:
            d[a].add(b)
            d[b].add(a)
        for a, b in zip(sentence1, sentence2):
            if not (a == b or a in d[b]):
                return False
        return True