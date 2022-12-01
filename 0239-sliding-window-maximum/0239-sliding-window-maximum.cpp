class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        multiset<int> s;
        int i = 0;
        while (i < k) s.insert(nums[i++]);
        vector<int> ans {*s.rbegin()};
        while (i < nums.size()) {
            s.erase(s.find(nums[i-k]));
            s.insert(nums[i++]);
            ans.emplace_back(*s.rbegin());
        }
        return ans;
    }
};