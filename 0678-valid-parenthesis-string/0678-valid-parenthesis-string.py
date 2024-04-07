class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        d = {}
        for l in range(n + 1):
            d['(' + '*' * l + ')'] = '*' * l
        # print(s)
        while True:
            s_ = s
            for k, v in d.items():
                s = s.replace(k, v)
            if s == s_:
                break
            # print(s)
        d2 = {'(*': '', '*)': ''}
        while True:
            s_ = s
            for k, v in d2.items():
                s = s.replace(k, v)
            if s == s_:
                break
            # print(s)
        return s == len(s) * '*'