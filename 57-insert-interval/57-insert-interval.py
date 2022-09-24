class Solution:
    def insert(self, ls: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, j = newInterval
        ans = []
        done = False
        for a, b in ls:
            if done:
                ans.append([a, b])
                continue
            if i < a: # [i, a-b]
                if j < a: # [i-j], [a-b]
                    ans.append([i, j])
                    ans.append([a, b])
                    done = True
                elif j <= b: # [i, a-j-b]
                    ans.append([i, b])
                    done = True
                else: # [i, a-b, j]
                    continue
            elif i <= b: # [a-i-b]
                if j <= b: # [a-i-j-b]
                    ans.append([a, b])
                    done = True
                else: # [a-i-b, j]
                    i = a
                    continue
            else: # [a-b, i]
                ans.append([a, b])
                continue
        if not done:
            ans.append([i, j])
        return ans
            