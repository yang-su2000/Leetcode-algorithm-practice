class Solution:
    def isValid(self, word: str) -> bool:
        if not len(word) >= 3:
            return False
        condition2 = True
        condition3 = False
        condition4 = False
        for c in word:
            if not (c.isnumeric() or c.isalpha()):
                condition2 = False
            if c in 'aeiouAEIOU':
                condition3 = True
            elif c.isalpha():
                condition4 = True
        return condition2 and condition3 and condition4