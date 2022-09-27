class Solution:
    def pushDominoes(self, d: str) -> str:
        ls = [] # idx
        n = len(d)
        ans = []
        for i, state in enumerate(d):
            if state != '.':
                ls.append(i)
            ans.append(state)
        while ls:
            # print(ls, ''.join(ans))
            states = defaultdict(int) # idx -> (1 left, 0 still, -1 right)
            for i in ls:
                if ans[i] == 'L':
                    if i >= 1:
                        states[i-1] -= 1
                elif ans[i] == 'R':
                    if i+1 < n:
                        states[i+1] += 1
            ls = []
            for i, state in states.items():
                if ans[i] != '.':
                    continue
                if state == -1:
                    ans[i] = 'L'
                    ls.append(i)
                elif state == 1:
                    ans[i] = 'R'
                    ls.append(i)
        return ''.join(ans)