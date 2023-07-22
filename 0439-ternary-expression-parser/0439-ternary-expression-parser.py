class Solution:
    def parseTernary(self, e: str) -> str:
        count = 0
        tf = []
        st = []
        i = 0
        n = len(e)
        while i < n:
            if i == n-1 or e[i+1] != '?':
                st.append(e[i])
                count -= 1
                while tf and tf[-1] == count:
                    tf.pop()
                    rval = st.pop()
                    lval = st.pop()
                    tfval = st.pop()
                    st.append(lval if tfval == 'T' else rval)
                    count -= 1
            else:
                tf.append(count)
                st.append(e[i])
                count += 2
            i += 2
        return str(st[0])