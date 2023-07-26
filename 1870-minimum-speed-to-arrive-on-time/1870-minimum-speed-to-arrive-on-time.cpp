class Solution {
public:
    int minSpeedOnTime(vector<int>& dist, double hour) {
        int n = (int) dist.size();
        int l = 1, r = 1e7 + 5;
        while (l < r) {
            int mid = (l + r) / 2;
            int val = 0;
            for (int i=0; i<n-1; i++) {
                val += (dist[i] + mid - 1) / mid;
            }
            if ((double) val + (double) dist[n-1] / mid <= hour) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        if (l == 1e7 + 5) return -1;
        return l;
    }
};