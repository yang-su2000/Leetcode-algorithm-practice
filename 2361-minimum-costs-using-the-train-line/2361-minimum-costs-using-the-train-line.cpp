#define ll long long

class Solution {
public:
    vector<ll> minimumCosts(vector<int>& a, vector<int>& b, int bcost) {
        int n = a.size();
        vector<ll> r1(n), r2(n), ret(n);
        r1[0] = min(a[0], b[0] + bcost);
        r2[0] = min(a[0], b[0]) + bcost;
        ret[0] = min(r1[0], r2[0]);
        for (int i=1; i<n; i++) {
            r1[i] = min(r1[i-1], r2[i-1]) + a[i];
            r2[i] = min(r1[i] + bcost, r2[i-1] + b[i]);
            ret[i] = min(r1[i], r2[i]);
        }
        return ret;
    }
};