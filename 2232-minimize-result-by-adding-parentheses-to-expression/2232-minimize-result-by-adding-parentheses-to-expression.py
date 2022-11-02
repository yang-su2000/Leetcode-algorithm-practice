class Solution:
    def minimizeResult(self, expr: str) -> str:
        mins = ''
        minval = float('inf')
        a, b = [i for i in expr.split('+')]
        al, bl = len(a), len(b)
        for i in range(al):
            for j in range(1, bl+1):
                s = a[:i] + '(' + a[i:] + '+' + b[:j] + ')' + b[j:]
                lval = int(a[:i]) if a[:i] else 1
                midval = int(a[i:]) + int(b[:j])
                rval = int(b[j:]) if b[j:] else 1
                val = lval * midval * rval
                if val < minval:
                    minval = val
                    mins = s
        return mins