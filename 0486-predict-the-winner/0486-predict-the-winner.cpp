class Solution {
public:
    bool rec(vector<int>& nums, int l, int r, int x, bool turn) {
        // cout << l << ", " << r << ", " << x << ", " << turn << endl;
        if (l > r) return x >= 0;
        if (turn) return 
            rec(nums, l + 1, r, x + nums[l], !turn) ||
            rec(nums, l, r - 1, x + nums[r], !turn);
        return rec(nums, l + 1, r, x - nums[l], !turn) &&
               rec(nums, l, r - 1, x - nums[r], !turn);
    }
    
    bool PredictTheWinner(vector<int>& nums) {
        return rec(nums, 0, nums.size() - 1, 0, true);
    }
};