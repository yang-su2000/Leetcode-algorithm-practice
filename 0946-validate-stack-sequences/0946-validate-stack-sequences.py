class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        j = 0
        s = []
        while i < len(pushed):
            s.append(pushed[i])
            i += 1
            while j < len(popped) and s and popped[j] == s[-1]:
                s.pop()
                j += 1
        return s == popped[j:][::-1]