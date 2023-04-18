class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        i = 0
        j = 0
        l1 = len(word1)
        l2 = len(word2)
        flag = True
        while i < l1 and j < l2:
            if flag:
                ans += word1[i]
                i += 1
            else:
                ans += word2[j]
                j += 1
            flag = not flag
        return ''.join(ans) + word1[i:] + word2[j:]