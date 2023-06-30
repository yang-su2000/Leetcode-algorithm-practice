class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> sub;
        int ans=0;
        for (int i=0; i<nums.size(); i++) {
            if (sub.empty() or nums[i] > sub.back()) {
                sub.push_back(nums[i]);
                ans = max((int) sub.size(), ans);
            } else {
                auto it = lower_bound(sub.begin(), sub.end(), nums[i]);
                if (it == sub.end()) continue;
                int d = it - sub.begin();
                sub[d] = nums[i];
            }
            // for (int &i:sub) printf("%d ", i);
            // printf("\n");
        }
        return ans;
    }
};