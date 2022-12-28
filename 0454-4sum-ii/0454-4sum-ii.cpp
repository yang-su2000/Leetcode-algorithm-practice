class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, \
                     vector<int>& nums3, vector<int>& nums4) {
        int n = nums1.size();
        int ans = 0;
        unordered_map<int, int> m;
        for (int &i: nums1) {
            for (int &j: nums2) {
                m[-i-j]++;
            }
        }
        for (int &k: nums3) {
            for (int &l: nums4) {
                if (m.count(k+l)) ans += m[k+l];
            }
        }
        return ans;
    }
};