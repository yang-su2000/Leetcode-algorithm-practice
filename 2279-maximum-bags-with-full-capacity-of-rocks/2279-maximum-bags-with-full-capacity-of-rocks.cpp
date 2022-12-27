class Solution {
public:
    int maximumBags(vector<int>& v, vector<int>& rocks, int r) {
        int n = v.size();
        int i;
        for (i=0; i<n; i++) v[i] -= rocks[i];
        sort(v.begin(), v.end());
        i = 0;
        while (i < n and v[i] <= r) r -= v[i++];
        return i;
    }
};