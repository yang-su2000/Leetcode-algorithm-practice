class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        bool has_one=false;
        for (int &i:nums) {
            if (i==1) {
                has_one=true;
            } else if (i<=0) i=1;
        }
        if (!has_one) return 1;
        nums.push_back(1);
        int n=nums.size();
        for (int &i:nums) {
            int j=abs(i);
            if (j<n and nums[j]>0) nums[j]*=-1;
        }
        for (int i=2; i<n; i++) {
            if (nums[i]>0) return i;
        }
        return n;
    }
};