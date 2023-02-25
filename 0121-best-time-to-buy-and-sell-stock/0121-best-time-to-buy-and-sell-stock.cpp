class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // int s0 = 0; // start state profit, always 0
        int s1 = INT_MIN; // buy state profit
        int ans = 0; // sell state profit
        for (int i: prices) {
            s1 = max(s1, -i);
            ans = max(ans, s1 + i);
        }
        return ans;
    }
};