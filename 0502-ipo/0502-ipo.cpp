class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pool; // capital (min), profits
        priority_queue<int> cur; // profits (max)
        int n = profits.size();
        for (int i=0; i<n; i++) {
            if (capital[i] <= w) cur.push(profits[i]);
            else pool.push({capital[i], profits[i]});
        }
        // cout << w << endl;
        while (k-- and !cur.empty()) {
            int max_profit = cur.top();
            cur.pop();
            w += max_profit;
            while (!pool.empty() and pool.top().first <= w) {
                cur.push(pool.top().second);
                pool.pop();
            }
            // cout << w << endl;
        }
        return w;
    }
};