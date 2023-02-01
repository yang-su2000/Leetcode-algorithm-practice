class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i = 0
        while i < len(str1) and i < len(str2) and str1[i] == str2[i]:
            i += 1
        while i:
            x = str1[:i]
            if len(str1) % len(x) == 0 and len(str2) % len(x) == 0:
                r1 = len(str1) // len(x)
                r2 = len(str2) // len(x)
                if x * r1 == str1 and x * r2 == str2:
                    return x
            i -= 1
        return ""