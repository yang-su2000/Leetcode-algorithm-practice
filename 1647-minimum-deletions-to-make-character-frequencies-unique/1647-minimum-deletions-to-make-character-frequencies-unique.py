class Solution:
    def minDeletions(self, s: str) -> int:
        
        d = Counter(s)
        s = set()
        ans = 0
        for count in d.values():
            while count in s and count > 0:
                count -= 1
                ans += 1
            s.add(count)
        return ans