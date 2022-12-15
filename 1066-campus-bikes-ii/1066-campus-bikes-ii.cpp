class Solution {
    vector<int> dp; // dp[bit(101)] = the ans (min dist) for pairing bit(101) in bikes and index(0, 1) in workers
    int n, m;
public:
    int get_dist(vector<vector<int>>& a, vector<vector<int>>& b, int ai, int bi) {
        if (ai == n) return 0;
        if (dp[bi] != -1) return dp[bi];
        int val = 20001;
        int b2, d;
        for (int i=0; i<m; i++) {
            b2 = bi | (1 << i);
            if (b2 == bi) continue;
            d = abs(a[ai][0] - b[i][0]) + abs(a[ai][1] - b[i][1]);
            val = min(val, get_dist(a, b, ai+1, b2) + d);
        }
        dp[bi] = val;
        return val;
    }
    
    int assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        n = workers.size();
        m = bikes.size();
        dp.resize(1 << m, -1);
        return get_dist(workers, bikes, 0, 0);
    }
};