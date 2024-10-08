class Solution:
    def minSwaps(self, s: str) -> int:
        st = []
        for c in s:
            if c == ']':
                if st and st[-1] == '[':
                    st.pop()
                else:
                    st.append(c)
            else:
                st.append(c)
        s = ''.join(st)
        # print(s)
        return (len(s) // 2 + 1) // 2