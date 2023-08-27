class TreeAncestor {
    int dp[int(5e4)+1][20]; // dp[i][j]: for node i, its 2^j th ancester idx
public:
    TreeAncestor(int n, vector<int>& parent) {
        memset(dp, -1, sizeof dp);
        for (int i=0; i<n; i++) {
            dp[i][0] = parent[i];
        }
        for (int b=1; b<20; b++) {
            for (int i=0; i<n; i++) {
                int p = dp[i][b-1];
                if (p != -1) dp[i][b] = dp[p][b-1];
            }
        }
    }
    
    int getKthAncestor(int node, int k) {
        int ans = node;
        for (int b=0; b<20; b++) {
            if (k & (1 << b)) {
                if (ans != -1) ans = dp[ans][b];
            }
        }
        return ans;
    }
};

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor* obj = new TreeAncestor(n, parent);
 * int param_1 = obj->getKthAncestor(node,k);
 */