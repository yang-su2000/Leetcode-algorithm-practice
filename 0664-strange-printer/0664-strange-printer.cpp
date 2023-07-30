class Solution {
public:
    int strangePrinter(string s) {
        int n = s.length();
        vector<vector<int>> memo(n, vector<int>(n, -1));
        function<int(int, int)> dp = [&](int l, int r) {
            if (l > r) return 0;
            if (l == r) return 1;
            if (memo[l][r] != -1) return memo[l][r];
            int ret = 1 + dp(l, r-1);
            for (int i=l+1; i<=r; i++) {
                if (s[i] == s[l]) {
                    ret = min(ret, dp(l+1, i-1) + dp(i, r));
                }
            }
            for (int i=r-1; i>=l; i--) {
                if (s[i] == s[r]) {
                    ret = min(ret, dp(l, i) + dp(i+1, r-1));
                }
            }
            memo[l][r] = ret;
            return ret;
        };
        return dp(0, n-1);
    }
};