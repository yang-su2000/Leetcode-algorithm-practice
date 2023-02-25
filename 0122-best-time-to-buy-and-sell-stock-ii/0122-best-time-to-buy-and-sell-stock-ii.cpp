class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int b = INT_MIN; // buy state profit
        int s = 0; // sell state profit
        for (int i: prices) {
            b = max(b, s - i);
            s = max(s, b + i);
        }
        return s;
    }
};