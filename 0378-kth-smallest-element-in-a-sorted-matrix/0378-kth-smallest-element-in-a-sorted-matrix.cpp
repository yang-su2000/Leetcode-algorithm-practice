class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        int m = matrix[0].size();
        int i = 0, j = m-1;
        int l = 0, r = n*m;
        while (0<=i and i<n and 0<=j and j<m) {
            int target = matrix[i][j];
            auto pos = getPos(target, matrix);
            if (pos.first <= k and k <= pos.second) return target;
            else if (pos.second < k) i++;
            else j--;
        }
        return matrix[i][j];
    }
    
    // get number of elements <= target in sorted mat
    pair<int, int> getPos(int target, vector<vector<int>>& mat) {
        int ans0 = 0;
        int ans1 = 0;
        for (auto &v:mat) {
            ans0 += lower_bound(v.begin(), v.end(), target) - v.begin();
            ans1 += upper_bound(v.begin(), v.end(), target) - v.begin();
        }
        return {ans0+1, ans1};
    }
};