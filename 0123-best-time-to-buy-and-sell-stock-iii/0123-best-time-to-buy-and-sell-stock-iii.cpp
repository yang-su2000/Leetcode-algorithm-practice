class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int b0 = INT_MIN; // buy state 0
        int s0 = 0; // sell state 0
        int b1 = INT_MIN; // buy state 1
        int s1 = 0; // sell state 1
        for (int i: prices) {
            b0 = max(b0, -i);
            s0 = max(s0, b0 + i);
            b1 = max(b1, s0 - i);
            s1 = max(s1, b1 + i);
        }
        return s1;
    }
};