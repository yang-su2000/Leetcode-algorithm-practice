class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        
        def valid_pres(word): # pres that suf = rsuf, O(k^2)
            pres = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    pres.append(word[:i])
            return pres
        
        def valid_sufs(word): # sufs that pre = rpre, O(k^2)
            sufs = []
            for i in range(len(word)):
                if word[:i+1] == word[:i+1][::-1]:
                    sufs.append(word[i+1:])
            return sufs
        
        d = {word: i for i, word in enumerate(words)}
        ans = []
        for idx, word in enumerate(words): # O(nk^2)
            rword = word[::-1]
            # case 1: word1, word2 => rword2, rword1
            # word1 = rword2
            # this word is word1
            if rword in d and d[rword] != idx:
                ans.append([idx, d[rword]])
            # case 2: word1, word2_pre, word2_suf => rword2_suf, rword2_pre, rword1
            # 1. word1 = rword2_suf
            # 2. word2_pre = rword2_pre
            # 3. word2_suf = rword1
            # notice 1. = 3.
            # this word is word2
            for suf in valid_sufs(word): # satisfy 2.
                rsuf = suf[::-1]
                if rsuf in d: # satisfy 1.
                    ans.append([d[rsuf], idx])
            # case 3: word1_pre, word1_suf, word2 => rword2, rword1_suf, rword1_pre
            # 1. word1_pre = rword2
            # 2. word1_suf = rword1_suf
            # 3. word2 = rword1_pre
            # notice 1. = 3.
            # this word is word1
            for pre in valid_pres(word): # satisfy 2.
                rpre = pre[::-1]
                if rpre in d: # satisfy 1.
                    ans.append([idx, d[rpre]])
        return ans