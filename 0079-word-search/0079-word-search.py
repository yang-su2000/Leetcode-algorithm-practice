class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        reversed(word)
        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(i, j, board, word, 0):
                    return True
        return False
    
    def dfs(self, i, j, board, word, word_i):
        if board[i][j] != word[word_i]:
            return False
        if word_i == len(word) - 1:
            return True
        letter = word[word_i]
        board[i][j] = '-'
        word_i += 1
        if i > 0 and self.dfs(i - 1, j, board, word, word_i):
            return True
        if i < self.m - 1 and self.dfs(i + 1, j, board, word, word_i):
            return True
        if j > 0 and self.dfs(i, j - 1, board, word, word_i):
            return True
        if j < self.n - 1 and self.dfs(i, j + 1, board, word, word_i):
            return True
        board[i][j] = letter
        return False