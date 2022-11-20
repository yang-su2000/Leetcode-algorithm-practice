class Solution:
    def calculate(self, s: str) -> int:
        lst = []
        cur = ''
        ops = set('-()')
        for c in s:
            if '0' <= c and c <= '9':
                cur += c
            elif cur != '':
                lst.append(int(cur))
                cur = ''
            if c in ops:
                lst.append(c)
        if cur != '':
            lst.append(int(cur))
            cur = ''
        # print(lst)
        
        stack = []
        for c in lst:
            if c == ')':
                val = stack.pop()
                stack[-1] = val
            else:
                stack.append(c)
            while isinstance(stack[-1], int) and len(stack) >= 2:
                if isinstance(stack[-2], int):
                    val = stack.pop()
                    stack[-1] += val
                elif stack[-2] == '-':
                    val = stack.pop()
                    stack[-1] = -val
                else:
                    break
            # print(stack)
            
        return stack[0]