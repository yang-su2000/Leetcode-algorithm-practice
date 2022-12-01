class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> d;
        vector<int> ans;
        for (int i=0; i<nums.size(); i++) {
            if (!d.empty() and d.front() == i-k) d.pop_front();
            while (!d.empty() and nums[d.back()] < nums[i]) d.pop_back();
            d.push_back(i);
            if (i >= k-1) ans.push_back(nums[d.front()]);
        }
        return ans;
    }
};