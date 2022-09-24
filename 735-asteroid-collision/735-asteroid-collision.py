class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        ans = []
        for i in asteroids:
            if i > 0:
                s.append(i)
            else:
                keep = True
                while s:
                    if s[-1] > -i:
                        keep = False
                        break
                    elif s[-1] == -i:
                        s.pop()
                        keep = False
                        break
                    else:
                        s.pop()
                if keep:
                    ans.append(i)
        return ans + s