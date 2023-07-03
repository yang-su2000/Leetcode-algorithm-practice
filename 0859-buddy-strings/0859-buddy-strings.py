class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        st = set()
        flag = False
        c1, c2 = None, None
        c3, c4 = None, None
        for a, b in zip(s, goal):
            if a in st:
                flag = True
            else:
                st.add(a)
            if a == b:
                continue
            if c1 is None:
                c1 = a
                c3 = b
            elif c2 is None:
                c2 = a
                c4 = b
            else:
                return False
        if c1 is None:
            return flag
        if c2 is None:
            return False
        return c1 == c4 and c2 == c3