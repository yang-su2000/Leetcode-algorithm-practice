class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = defaultdict(lambda: 0)
        ans = 0
        for word in sorted(words):
            word2 = word[1] + word[0]
            if word2 in d:
                ans += 4
                d[word2] -= 1
                if d[word2] == 0:
                    del d[word2]
            else:
                d[word] += 1
        # print(d.items())
        add = False
        for word in d.keys():
            if word[0] == word[1]:
                add = True
                break
        return ans + (2 if add else 0)