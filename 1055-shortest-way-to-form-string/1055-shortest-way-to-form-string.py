class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ans = 0
        j = len(source)
        for c in target:
            while j < len(source):
                if source[j] == c:
                    break
                else:
                    j += 1
            if j == len(source):
                ans += 1
                invalid = True
                for j in range(len(source)):
                    if source[j] == c:
                        invalid = False
                        j += 1
                        break
                if invalid:
                    return -1
            else:
                j += 1
        return ans