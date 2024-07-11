class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans = []
        for c in list(s):
            if c == '(':
                ans.append(c)
            elif c == ')':
                if ans[-1] == '(':
                    ans.pop()
                    continue
                s = ans.pop()[::-1]
                ans.pop()
                while ans and ans[-1] != '(':
                    s = ans.pop() + s
                ans.append(s)
            else:
                if ans and ans[-1] != '(':
                    ans[-1] = ans[-1] + c
                else:
                    ans.append(c)
            # print(ans)
        return ans[0]