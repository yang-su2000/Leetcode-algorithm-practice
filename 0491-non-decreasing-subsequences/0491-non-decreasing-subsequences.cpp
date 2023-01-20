class Solution {
    
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        set<vector<int>> ans;
        int n = nums.size();
        int max_count = (1 << n);
        for (int i=0; i<max_count; i++) {
            vector<int> cur;
            for (int j=0; j<n; j++) {
                if (i & (1 << j)) {
                    if (cur.empty() or cur.back() <= nums[j]) cur.push_back(nums[j]);
                }
            }
            if (cur.size() >= 2) ans.insert(cur);
        }
        return vector(ans.begin(), ans.end());
    }
};