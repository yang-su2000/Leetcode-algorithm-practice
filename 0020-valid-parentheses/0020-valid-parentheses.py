class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in ('(', '[', '{'):
                st.append(c)
            elif st and st[-1] + c in ('()', '[]', '{}'):
                st.pop()
            else:
                return False
        return not st