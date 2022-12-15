class Solution {
    int ans = 20001;
    int n, m;
public:
    // a: i, b: used
    void get_dist(vector<vector<int>>& a, vector<vector<int>>& b, vector<bool>& used, int ai, int bi, int d) {
        if (ai == n) {
            ans = min(ans, d);
            return;
        }
        while (used[bi]) bi++;
        int d2;
        for (int i=bi; i<m; i++) {
            if (used[i]) continue;
            used[i] = true;
            d2 = abs(a[ai][0] - b[i][0]) + abs(a[ai][1] - b[i][1]);
            get_dist(a, b, used, ai+1, bi, d+d2);
            used[i] = false;
        }
    }
    
    int assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        n = workers.size();
        m = bikes.size();
        vector<bool> used(n);
        get_dist(workers, bikes, used, 0, 0, 0);
        return ans;
    }
};