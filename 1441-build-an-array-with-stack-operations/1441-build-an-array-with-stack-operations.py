class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        m = len(target)
        for i in range(m):
            l = target[i-1] if i else 0
            r = target[i]
            ans.extend(["Push", "Pop"] * (r - l - 1))
            ans.append("Push")
        return ans