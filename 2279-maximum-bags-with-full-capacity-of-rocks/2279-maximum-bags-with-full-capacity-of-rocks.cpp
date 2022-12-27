class Solution {
public:
    int maximumBags(vector<int>& capacity, vector<int>& rocks, int additionalRocks) {
        int n = capacity.size();
        vector<int> v(n);
        int i;
        for (i=0; i<n; i++) v[i] = capacity[i] - rocks[i];
        sort(v.begin(), v.end());
        i = 0;
        while (i < n and v[i] <= additionalRocks) additionalRocks -= v[i++];
        return i;
    }
};