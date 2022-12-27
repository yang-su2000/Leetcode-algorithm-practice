class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        int m = matrix[0].size();
        int i = 0, j = m-1;
        while (0<=i and i<n and 0<=j and j<m) {
            int target = matrix[i][j];
            // l: get number of elements < target in sorted mat
            // r: get number of elements <= target in sorted mat
            int l = 0, r = 0;
            for (auto &v:matrix) {
                l += lower_bound(v.begin(), v.end(), target) - v.begin();
                r += upper_bound(v.begin(), v.end(), target) - v.begin();
            }
            if (l + 1 <= k and k <= r) return target;
            else if (r < k) i++;
            else j--;
        }
        return matrix[i][j];
    }
};