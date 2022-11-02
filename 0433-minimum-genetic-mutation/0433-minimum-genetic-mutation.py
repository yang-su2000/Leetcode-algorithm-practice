class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        cur = [start]
        bank = set(bank)
        choices = set(['A','C','G','T'])
        ans = 0
        while cur:
            ans += 1
            nxt = []
            for s in cur:
                for i in range(len(s)):
                    for c in choices:
                        if s[i] == c:
                            continue
                        s_mut = s[:i] + c + s[i+1:]
                        if s_mut not in bank:
                            continue
                        if s_mut == end:
                            return ans
                        nxt.append(s_mut)
                        bank.remove(s_mut)
            cur = nxt
            # print(cur)
        return -1