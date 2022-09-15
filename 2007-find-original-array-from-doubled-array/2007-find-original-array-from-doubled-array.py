class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2:
            return []
        maxval = max(changed)
        counts = [0] * (min(10**5, maxval) + 1)
        for i in changed:
            counts[i] += 1
        ans = []
        while maxval:
            freq = counts[maxval]
            if not freq:
                maxval -= 1
                continue 
            if maxval % 2 == 0 and counts[maxval//2] >= freq:
                ans.extend([maxval//2] * freq)
                counts[maxval//2] -= freq
            else:
                return []
            maxval -= 1
        if counts[0]:
            if counts[0] % 2 == 0:
                ans.extend([0] * (counts[0]//2))
            else:
                return []
        return ans