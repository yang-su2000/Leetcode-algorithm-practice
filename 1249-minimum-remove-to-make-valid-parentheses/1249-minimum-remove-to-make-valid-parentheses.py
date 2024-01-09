class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == ')' and st and st[-1][0] == '(':
                st.pop()
            else:
                st.append((c, i))
        # print(st)
        ans = []
        j = 0
        for i, c in enumerate(s):
            if j < len(st) and i == st[j][1]:
                j += 1
            else:
                ans.append(c)
        return "".join(ans)