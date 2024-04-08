class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        ans = True
        n = len(preorder)
        i = 1
        st = [(preorder[0], -inf, inf)] # (val, lbound, rbound)
        while i < n:
            val = preorder[i]
            while st:
                if val < st[-1][1]:
                    return False
                if val > st[-1][2]:
                    st.pop()
                else:
                    break
            if val < st[-1][0]:
                st.append((val, st[-1][1], st[-1][0]))
            else:
                st.append((val, st[-1][0], st[-1][2]))
            # print(i, st)
            i += 1
        return True