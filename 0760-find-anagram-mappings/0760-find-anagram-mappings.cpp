class Solution {
public:
    vector<int> anagramMappings(vector<int>& nums1, vector<int>& nums2) {
        map<int, vector<int>> m;
        int n = nums1.size();
        for (int i=0; i<n; i++) {
            m[nums2[i]].push_back(i);
        }
        vector<int> ans(n);
        for (int i=0; i<n; i++) {
            int val = nums1[i];
            ans[i] = m[val].back();
            m[val].pop_back();
        }
        return ans;
    }
};