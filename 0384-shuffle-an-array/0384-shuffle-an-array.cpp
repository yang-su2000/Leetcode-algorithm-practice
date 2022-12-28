class Solution {
    vector<int> v;
    vector<int> v2;
public:
    Solution(vector<int>& nums) {
        v2 = v = nums;
    }
    
    vector<int> reset() {
        return v;
    }
    
    vector<int> shuffle() {
        swap(v2[rand() % v2.size()], v2[rand() % v2.size()]);
        return v2;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */