class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        lo = -inf
        st = []
        for val in preorder:
            while st and st[-1] < val:
                lo = max(lo, st.pop())
            if val < lo:
                return False
            st.append(val)
        return True
                