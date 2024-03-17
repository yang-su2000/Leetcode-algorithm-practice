class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        # optimized
        start_idxs = [] # current start indexes
        ans = 0
        for end_idx in range(len(s)):
            if s[end_idx] == c:
                start_idxs.append(end_idx)
                ans += len(start_idxs)
                # print(end_idx, start_idxs, ans)
        # print()
        # s = "abada" c = "a"
        # end_idx = 0, start_idxs = [0], ans += 1
        # "[a]bada"
        # end_idx = 2, start_idxs = [0, 2], ans += 2
        # "[aba]da", "ab[a]da"
        # end_idx = 4, start_idxs = [0, 2, 4], ans += 3
        # "[abada]", "ab[ada]", "abad[a]"
        
        # final math
        start_idxs_count = 0 # number of current start indexes
        ans = 0
        for end_idx in range(len(s)):
            if s[end_idx] == c:
                start_idxs_count += 1
                ans += start_idxs_count
        return ans