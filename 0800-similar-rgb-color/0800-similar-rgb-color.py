class Solution:
    def similarRGB(self, color: str) -> str:
        a, b, c = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
        # print(a, b, c)
        ans = ''
        sim = float('-inf')
        for A in range(16):
            a2 = A * 16 + A
            for B in range(16):
                b2 = B * 16 + B
                for C in range(16):
                    c2 = C * 16 + C
                    cur = -(a2 - a)**2 - (b2 - b)**2 - (c2 - c)**2
                    if cur > sim:
                        sim = cur
                        ans = self.toString(A, B, C)
        return ans
    
    def toString(self, a, b, c):
        pre = '#'
        a = str(a) if a < 10 else chr(ord('a') + (a - 10))
        b = str(b) if b < 10 else chr(ord('a') + (b - 10))
        c = str(c) if c < 10 else chr(ord('a') + (c - 10))
        return pre + a + a + b + b + c + c