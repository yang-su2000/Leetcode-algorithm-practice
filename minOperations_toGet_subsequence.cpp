class Solution {
public:
    // find first index bigger than p
    int bSearch(vector<int>& dp, int p) {
        int l=0, r=dp.size()-1;
        while (l<r) {
            int mid = l+(r-l)/2;
            if (dp[mid]<p) l = mid+1;
            else r = mid;
        }
        return l;
    }

    int minOperations(vector<int>& target, vector<int>& arr) {
        map<int, int> target_map;
        for (int i=0; i<target.size(); i++) target_map[target[i]] = i;
        vector<int> arr2;
        for (int &i:arr){
            if (target_map.count(i)) arr2.emplace_back(target_map[i]);
        }
        // reduced to 最长递增子序列 (LIS)
        vector<int> dp;
        if (!arr2.empty()) dp.emplace_back(arr2[0]);
        else return target.size();
        for (int i=1; i<arr2.size(); i++){
            if (arr2[i]>dp.back()) dp.emplace_back(arr2[i]);
            else {
                int idx = bSearch(dp, arr2[i]);
                dp[idx] = arr2[i];
            }
        }
        cout << "arr2: ";
        for (int &i:arr2) cout << i << " ";
        cout << endl << "dp: ";
        for (int &i:dp) cout << i << " ";
        return target.size()-dp.size();
    }
};