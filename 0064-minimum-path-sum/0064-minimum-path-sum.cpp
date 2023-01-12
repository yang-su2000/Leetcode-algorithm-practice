class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int cur;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                cur = INT_MAX;
                if (i > 0) cur = grid[i][j] + grid[i-1][j];
                if (j > 0) cur = min(cur, grid[i][j] + grid[i][j-1]);
                if (cur == INT_MAX) cur = grid[i][j];
                grid[i][j] = cur;
            }
        }
        return grid[m-1][n-1];
    }
};