class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        vector<int> b(k, INT_MIN); // buy states
        vector<int> s(k, 0); // sell states
        int i;
        for (int p: prices) {
            i = 0;
            while (i < k) {
                if (i == 0) b[i] = max(b[i], -p);
                else b[i] = max(b[i], s[i-1] - p);
                s[i] = max(s[i], b[i] + p);
                i++;
            }
        }
        return s[k-1];
    }
};