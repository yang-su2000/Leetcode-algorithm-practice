#define ll long long

class Solution {
public:
    int numberOfWays(int numPeople) {
        vector<ll> dp(numPeople + 1);
        dp[0] = 1;
        int i = 2;
        int mod = 1e9+7;
        while (i <= numPeople) {
            for (int a=0, b=i-2; a<i; a+=2, b-=2) {
                dp[i] = (dp[i] + dp[a] * dp[b]) % mod;
            }
            i += 2;
        }
        return dp[numPeople];
    }
};