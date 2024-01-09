class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        def split(s):
            cur = []
            ret = []
            for c in s:
                if not cur:
                    cur.append(c)
                elif c.isdigit() ^ cur[-1].isdigit():
                    ret.append("".join(cur))
                    cur = [c]
                else:
                    cur.append(c)
            if cur:
                ret.append("".join(cur))
            return ret
        
        ls = split(abbr)
        # print(ls)
        i = 0
        j = 0
        while i < len(word) and j < len(ls):
            piece = ls[j]
            if piece.isdigit():
                val = int(piece)
                if not val or str(val) != piece:
                    return False
                i += val
                j += 1
            else:
                if word[i:i+len(piece)] != piece:
                    return False
                i += len(piece)
                j += 1
        return i == len(word) and j == len(ls)