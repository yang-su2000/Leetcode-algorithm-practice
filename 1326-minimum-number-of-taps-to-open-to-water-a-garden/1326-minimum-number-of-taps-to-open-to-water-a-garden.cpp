class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        vector<int> p(n + 1);
        for (int i=0; i<=n; i++) {
            int l = max(0, i - ranges[i]);
            int r = min(n, i + ranges[i]);
            p[l] = max(p[l], r);
        }
        int r2 = 0;
        int r = 0;
        int ans = 0;
        for (int l=0; l<=n; l++) {
            if (l > r2) return -1;
            if (l > r) {
                ans++;
                r = r2;
            }
            r2 = max(r2, p[l]);
        }
        return ans;
    }
};