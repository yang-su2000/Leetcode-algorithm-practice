class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # (c, count)
        c = s[0]
        count = 1
        ans = ''
        for i in s[1:] + '$':
            if i == c:
                count += 1
            else:
                if stack and stack[-1][0] == c:
                    stack[-1] = (c, stack[-1][1] + count)
                else:
                    stack.append((c, count))
                c = i
                count = 1
            while stack and stack[-1][1] >= k:
                c2, count2 = stack.pop()
                count2 %= k
                if count2:
                    stack.append((c2, count2))
        for c2, count2 in stack:
            ans += c2 * count2
        return ans