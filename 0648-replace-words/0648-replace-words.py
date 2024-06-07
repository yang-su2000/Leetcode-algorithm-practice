class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d = set(dictionary)
        ans = []
        for word in sentence.split():
            done = False
            for i in range(1, len(word)):
                if word[:i] in d:
                    ans.append(word[:i])
                    done = True
                    break
            if not done:
                ans.append(word)
        return ' '.join(ans)