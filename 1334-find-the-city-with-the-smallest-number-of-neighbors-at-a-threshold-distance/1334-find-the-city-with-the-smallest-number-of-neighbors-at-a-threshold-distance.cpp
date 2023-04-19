class Solution {
public:
    int findTheCity(int n, vector<vector<int>>& edges, int d) {
        vector<vector<int>> A(n, vector<int>(n, 1e4+1));
        for (auto &v: edges) {
            A[v[0]][v[1]] = v[2];
            A[v[1]][v[0]] = v[2];
        }
        for (int i=0; i<n; i++) A[i][i] = 0;
        for (int k=0; k<n; k++) {
            for (int i=0; i<n; i++) {
                for (int j=0; j<n; j++) {
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j]);
                }
            }
        }
        int ans = -1;
        int count = INT_MAX;
        for (int i=0; i<n; i++) {
            int cur = 0;
            for (int j=0; j<n; j++) {
                if (A[i][j] <= d) cur++;
            }
            if (cur <= count) {
                count = cur;
                ans = i;
            }
        }
        return ans;
    }
};