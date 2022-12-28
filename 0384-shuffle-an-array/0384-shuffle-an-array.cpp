class Solution {
    vector<int> v;
    random_device rd;
    mt19937 gen;
    uniform_int_distribution<> uni;
public:
    Solution(vector<int>& nums) {
        v = nums;
        gen = mt19937 {rd()};
        uni = uniform_int_distribution<> (0, v.size()-1);
    }
    
    vector<int> reset() {
        return v;
    }
    
    vector<int> shuffle() {
        vector<int> ret(v.size(), INT_MAX);
        int p;
        for (int i:v) {
            int p = uni(gen);
            while (1) {
                p = uni(gen);
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