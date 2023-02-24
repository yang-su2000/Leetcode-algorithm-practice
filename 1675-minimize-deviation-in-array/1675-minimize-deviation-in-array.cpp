#define ll long long

class Solution {
public:
    int minimumDeviation(vector<int>& nums) {
        set<pair<ll, ll>> s;
        for (int i: nums) {
            ll lo = (i >> __builtin_ctz(i));
            ll hi = i;
            if (hi & 1) hi <<= 1;
            s.insert({lo, hi});
        }
        if (s.size() == 1) return 0;
        // for (auto p: s) cout << p.first << " " << p.second << ", ";
        // cout << endl;
        ll ans = INT_MAX;
        while (s.size() > 1) {
            auto it = s.begin();
            ll top = s.rbegin()->first;
            ll lo = it->first;
            ll hi = it->second;
            s.erase(it);
            ans = min(ans, top - lo);
            if (lo == hi) return ans;
            s.insert({lo * 2, hi});
            // for (auto p: s) cout << p.first << " " << p.second << ", ";
            // cout << endl;
        }
        return ans;
    }
};