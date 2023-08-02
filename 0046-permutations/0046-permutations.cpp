class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        function<void(vector<int>&, int)> get = [&](vector<int>& cur, int taken) {
            if (cur.size() == nums.size()) {
                ans.push_back(cur);
                return;
            }
            for (int i=0; i<nums.size(); i++) {
                if (!((1 << i) & taken)) {
                    cur.push_back(nums[i]);
                    get(cur, taken | (1 << i));
                    cur.pop_back();
                }
            }
        };
        vector<int> tmp;
        get(tmp, 0);
        return ans;
    }
};