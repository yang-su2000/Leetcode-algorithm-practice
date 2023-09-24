class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        vector<vector<double>> dp(query_row+1, vector<double>(query_row+1));
        dp[0][0]=poured;
        for (int i=0; i<query_row; i++){
            for (int j=0; j<query_row; j++){
                if (dp[i][j]==0) continue;
                if (dp[i][j]>1) {
                    double flow=(dp[i][j]-1)/2;
                    dp[i+1][j]+=flow;
                    dp[i+1][j+1]+=flow;
                }
            }
        }
#if 0
        for (int i=0; i<=query_row; i++){
            for (int j=0; j<=query_row; j++) cout << dp[i][j] << " ";
            cout << endl;
        }
#endif
        return dp[query_row][query_glass]>1 ? 1 : dp[query_row][query_glass];
    }
};