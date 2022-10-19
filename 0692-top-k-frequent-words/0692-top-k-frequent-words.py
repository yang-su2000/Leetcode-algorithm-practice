class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(list)
        for word, count in Counter(words).items():
            d[count].append(word)
        for count, ls in d.items():
            ls.sort()
        l = sorted(d.items(), reverse=True)
        ans = []
        for count, ls in l:
            ans += ls
        return ans[:k]