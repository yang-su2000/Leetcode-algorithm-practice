class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size();
        int n = board[0].size();
        vector<pair<int, int>> d {{-1, 0}, {0, -1}, {1, 0}, {0, 1},
                                  {-1, -1}, {-1, 1}, {1, -1}, {1, 1}};
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                int nei = 0;
                for (auto &[di, dj]: d) {
                    int i2 = i+di;
                    int j2 = j+dj;
                    if (0 <= i2 and i2 < m and 0 <= j2 and j2 < n) {
                        if (board[i2][j2] % 2) nei++;
                    }
                }
                if (nei < 2 or nei > 3) board[i][j] += 2; // die
                else if (nei == 2 and !board[i][j]) board[i][j] += 2; // keep die
            }
        }
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (board[i][j] >= 2) board[i][j] = 0;
                else board[i][j] = 1;
            }
        }
    }
};