class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ans;
        int n=nums.size();
        if (!n) return ans;
        int l=nums[0], i=1, r=l;
        while (i<n){
            if (nums[i]==r+1) r++;
            else if (l==r) {
                ans.push_back(to_string(l));
                l=r=nums[i];
            } else {
                ans.push_back(to_string(l)+"->"+to_string(r));
                l=r=nums[i];
            }
            i++;
        }
        if (l==r) ans.push_back(to_string(l));
        else ans.push_back(to_string(l)+"->"+to_string(r));
        return ans;
    }
};