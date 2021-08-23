class Solution {
public:
    void twoSum(vector<int>& nums, int i, vector<vector<int>> &res){
        int lo=i+1, hi=nums.size()-1;
        while (lo<hi){
            int sum=nums[i]+nums[lo]+nums[hi];
            if (sum<0 or (lo>i+1 && nums[lo]==nums[lo-1])) lo++;
            else if (sum>0 or (hi<nums.size()-1 && nums[hi]==nums[hi+1])) hi--;
            else res.push_back({nums[i],nums[lo++],nums[hi--]});
        }
    }
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n=nums.size();
        sort(begin(nums),end(nums));
        vector<vector<int>> res;
        for (int i=0; i<n && nums[i]<=0; i++){
            if (i==0 or nums[i-1]!=nums[i]) twoSum(nums, i, res);
        }
        return res;
    }
};