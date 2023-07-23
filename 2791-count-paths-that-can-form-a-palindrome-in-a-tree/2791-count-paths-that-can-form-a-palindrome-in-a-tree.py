class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)
        A = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            A[p].append(i)
        ans = 0
        d = defaultdict(int)
        
        def dfs(node, xor):
            nonlocal ans, d, A
            xor ^= 1 << (ord(s[node]) - ord('a'))
            if xor ^ 0 in d:
                ans += d[xor ^ 0]
            for i in range(26):
                target = xor ^ (1 << i)
                if target in d:
                    ans += d[target]
            d[xor] += 1
            for child in A[node]:
                dfs(child, xor)
        
        dfs(0, 0)
        return ans
            