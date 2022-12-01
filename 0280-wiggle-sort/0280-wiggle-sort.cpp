class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> ans;
        int l = 0;
        int r = nums.size()-1;
        while (l < r) {
            ans.emplace_back(nums[l++]);
            ans.emplace_back(nums[r--]);
        }
        if (l == r) ans.emplace_back(nums[l]);
        swap(ans, nums);
    }
};