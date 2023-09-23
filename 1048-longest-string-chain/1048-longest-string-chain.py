class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def check(a, b):
            if len(a) + 1 != len(b):
                return False
            ai = 0
            bi = 0
            flag = False
            while ai < len(a) and bi < len(b):
                if a[ai] == b[bi]:
                    ai += 1
                    bi += 1
                else:
                    if flag:
                        return False
                    flag = True
                    bi += 1
            if ai < len(a):
                return False
            return True
        
        A = []
        n = len(words)
        for i in range(n):
            cur = [j for j in range(n) if check(words[i], words[j])]
            A.append(cur)
        # print(A)
        
        @cache
        def bfs(i):
            nonlocal A, n
            if not A[i]:
                return 1
            return 1 + max(bfs(j) for j in A[i])
        
        return max(bfs(i) for i in range(n))