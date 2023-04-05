class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        st = [] # (count, vsum)
        for i in nums[::-1]:
            if not st:
                st.append((1, i))
                continue
            else:
                count, vsum = st[-1]
                val = vsum / count
                if i > val:
                    st.append((1, i))
                else:
                    st[-1] = (count + 1, vsum + i)
                    while len(st) >= 2:
                        count, vsum = st[-1]
                        count2, vsum2 = st[-2]
                        if vsum / count <= vsum2 / count2:
                            st.pop()
                            st[-1] = (count + count2, vsum + vsum2)
                        else:
                            break
        count, vsum = st[-1]
        return vsum // count + (1 if vsum % count else 0)
                            
            
                    
        