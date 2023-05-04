class Solution:
    def predictPartyVictory(self, s: str) -> str:
        ls = [c for c in s]
        while ls:
            # print(ls)
            R = deque()
            D = deque()
            r = 0
            d = 0
            for i, c in enumerate(ls):
                if c == 'R':
                    if d:
                        d -= 1
                    else:
                        r += 1
                        R.append(i)
                else:
                    if r:
                        r -= 1
                    else:
                        d += 1
                        D.append(i)
            while r and D:
                D.popleft()
                r -= 1
            while d and R:
                R.popleft()
                d -= 1
            if not R:
                return 'Dire'
            if not D:
                return 'Radiant'
            ls = []
            while R and D:
                if R[0] < D[0]:
                    R.popleft()
                    ls.append('R')
                else:
                    D.popleft()
                    ls.append('D')
            ls.extend(['R'] * len(R))
            ls.extend(['D'] * len(D))