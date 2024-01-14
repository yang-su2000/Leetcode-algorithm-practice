class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        LEN_S = len(s)
        LEN_A = len(a)
        LEN_B = len(b)
        
        aa = []
        for i in range(LEN_S - LEN_A + 1):
            if s[i: i + LEN_A] == a:
                aa.append(i)
                
        bb = []
        for i in range(LEN_S - LEN_B + 1):
            if s[i: i + LEN_B] == b:
                bb.append(i)        
        
        res = []
        # print(bb)
        for idx in aa:
            l = bisect_left(bb, idx - k)
            r = bisect_right(bb, idx + k) - 1
            # print(idx, l, r)
            if l <= r:
                res.append(idx)
        
        return res