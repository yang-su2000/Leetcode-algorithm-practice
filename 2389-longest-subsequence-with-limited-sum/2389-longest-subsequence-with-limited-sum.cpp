class Solution {
public:
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int csum = 0;
        for (int i=0; i<n; i++) {
            csum += nums[i];
            nums[i] = csum;
        }
        vector<int> ans;
        for (int &q:queries) {
            int p = upper_bound(nums.begin(), nums.end(), q) - nums.begin();
            ans.push_back(p);
        }
        return ans;
    }
};