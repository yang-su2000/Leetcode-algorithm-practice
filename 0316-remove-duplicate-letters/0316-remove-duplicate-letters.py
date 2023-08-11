class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_d = {c: i for i, c in enumerate(s)}
        st = []
        for i, c in enumerate(s):
            if c in st:
                continue
            while st and st[-1] > c and i < last_d[st[-1]]:
                st.pop()
            st.append(c)
        return ''.join(st)