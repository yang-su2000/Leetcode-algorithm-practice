class Solution {
    vector<int> v;
public:
    Solution(vector<int>& nums) {
        v = nums;
    }
    
    vector<int> reset() {
        return v;
    }
    
    vector<int> shuffle() {
        vector<int> ret(v.size(), INT_MAX);
        int p;
        for (int i:v) {
            while (1) {
                p = rand() % (v.size());
                if (ret[p] == INT_MAX) break;
            }
            ret[p] = i;
        }
        return ret;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */