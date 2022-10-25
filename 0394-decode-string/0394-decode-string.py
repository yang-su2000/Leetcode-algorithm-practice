class Solution:
    def decodeString(self, s: str) -> str:
        ans = ''
        lst = [] # (num, ans_l)
        l = -1
        i = 0
        while i < len(s):
            if s[i] >= '0' and s[i] <= '9':
                if l == -1:
                    l = i
            elif s[i] == '[':
                num = int(s[l:i])
                lst.append((num, len(ans)))
                l = -1
            elif s[i] == ']':
                num, ans_l = lst.pop()
                ans = ans[:ans_l] + ans[ans_l:] * num
            else:
                ans += s[i]
            i += 1
        return ans
                
                    
                