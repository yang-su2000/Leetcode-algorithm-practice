class Solution {
public:
    int minimumAverageDifference(vector<int>& nums) {
        long lsum = nums[0];
        long rsum = 0;
        int n = nums.size();
        for (int i=1; i<n; i++) rsum += nums[i];
        long gmin = abs(lsum / 1);
        if (n-1) gmin = abs(lsum / 1 - rsum / (n-1));
        int gidx = 0;
        // cout << lsum << " " << rsum << " " << gmin << " " << gidx << endl;
        for (int i=1; i<n; i++) {
            lsum += nums[i];
            rsum -= nums[i];
            long cmin = abs(lsum / (i+1));
            if (n-i-1) cmin = abs(lsum / (i+1) - rsum / (n-i-1));
            if (cmin < gmin) {
                gmin = cmin;
                gidx = i;
                // cout << lsum << " " << rsum << " " << gmin << " " << gidx << endl;
            }
        }
        return gidx;
    }
};