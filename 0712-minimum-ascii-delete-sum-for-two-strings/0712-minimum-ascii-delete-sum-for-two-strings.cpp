class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        int n1 = s1.length();
        int n2 = s2.length();
        vector<vector<int>> memo(n1, vector<int>(n2, -1));
        function<int(int, int)> dp = [&](int i, int j) {
            int ret = 0;
            if (i >= n1 || j >= n2) {
                while (i < n1) ret += s1[i++];
                while (j < n2) ret += s2[j++];
                return ret;
            }
            if (memo[i][j] != -1) return memo[i][j];
            if (s1[i] == s2[j]) {
                ret = dp(i + 1, j + 1);
            } else {
                ret = min(s1[i] + dp(i + 1, j), s2[j] + dp(i, j + 1));
            }
            memo[i][j] = ret;
            return ret;
        };
        return dp(0, 0);
    }
};