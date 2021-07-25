class Solution {
public:
    int jumpFloor(int number) {
        vector<int> dp(number+1);
        dp[0]=1;
        for (int i = 1; i <= number; i++){
            if (i >= 1) dp[i] += dp[i-1];
            if (i >= 2) dp[i] += dp[i-2];
        }
        return dp[number];
    }
};