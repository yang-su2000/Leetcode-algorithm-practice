class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        los = []
        his = []
        bounds = []
        
        lo = []
        hi = []
        l = 10**5 + 1
        r = -1
        
        for idx, i in enumerate(nums):
            if i < minK or i > maxK:
                if hi and lo:
                    los.append(lo)
                    his.append(hi)
                    bounds.append((l, r))
                lo = []
                hi = []
                l = 10**5 + 1
                r = -1
                continue
            else:
                l = min(l, idx)
                r = max(r, idx)
            if i == minK:
                lo.append(idx)
            if i == maxK:
                hi.append(idx)
        if hi and lo:
            los.append(lo)
            his.append(hi)
            bounds.append((l, r))
        print(los, his, bounds)
        
        ans = 0
        for i in range(len(los)):
            lo, hi = los[i], his[i]
            l, r = bounds[i]
            loi, hii = 0, 0
            for j in range(l, r+1):
                while hii < len(hi) and loi < len(lo):
                    if lo[loi] < j:
                        loi += 1
                    elif hi[hii] < j:
                        hii += 1
                    else:
                        break
                if loi == len(lo) or hii == len(hi):
                    break
                ans += r - max(lo[loi], hi[hii]) + 1
                # print(ans)
        
        return ans
        
        