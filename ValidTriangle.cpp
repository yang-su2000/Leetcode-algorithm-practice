class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        // two pointer/bSearch + sort, O(n^2/n^2logn)
        sort(nums.begin(), nums.end());
        int ans=0;
        int i, j, n=nums.size();
        for (int i=0; i<n; ++i) {
            int k = i; // left pointer
            for (int j=i+1; j<n; ++j) { // right pointer
                while (k < n-1 && nums[k+1] < nums[i] + nums[j]) {
                    ++k;
                }
                ans += max(k-j, 0);
            }
        }
        return ans;
    }
};