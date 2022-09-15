from sortedcontainers import SortedDict

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2:
            return []
        d = SortedDict()
        for i in changed:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        ans = []
        while d:
            num, count = d.popitem()
            if num == 0:
                if count%2 == 0:
                    ans.extend([0] * (count//2))
                else:
                    return []
            elif num%2 == 0 and num//2 in d and d[num//2] >= count:
                d[num//2] -= count
                if d[num//2] == 0:
                    del d[num//2]
                ans.extend([num//2] * count)
            else:
                return []
        return ans
                