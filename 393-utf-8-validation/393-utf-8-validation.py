class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        ls = []
        for i in data:
            s = format(i, 'b')
            ls.append('0' * (8 - len(s)) + s)
        print(ls)
        n = len(ls)
        i = 0
        while i < n:
            if ls[i][0] == '0':
                i += 1
            elif ls[i][:2] == '10':
                return False
            elif ls[i][:3] == '110':
                if i + 1 < n and ls[i+1][0:2] == '10':
                    i += 2
                else:
                    return False
            elif ls[i][:4] == '1110':
                if i + 2 < n and ls[i+1][:2] == ls[i+2][:2] == '10':
                    i += 3
                else:
                    return False
            elif ls[i][:5] == '11110':
                if i + 3 < n and ls[i+1][:2] == ls[i+2][:2] == ls[i+3][:2] == '10':
                    i += 4
                else:
                    return False
            else:
                return False
        return True