class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& mat) {
        int n = mat.size();
        int i, j, pmin;
        for (i=1; i<n; i++) {
            for (j=0; j<n; j++) {
                pmin = mat[i-1][j];
                if (j) pmin = min(pmin, mat[i-1][j-1]);
                if (j < n-1) pmin = min(pmin, mat[i-1][j+1]);
                mat[i][j] += pmin;
            }
        }
        int ans = INT_MAX;
        for (j=0; j<n; j++) ans = min(ans, mat[n-1][j]);
        return ans;
    }
};