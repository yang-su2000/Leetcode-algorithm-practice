#define ll long long

class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, ll success) {
        sort(potions.begin(), potions.end());
        int n = spells.size();
        vector<int> ans(n);
        for (int i=0; i<n; i++) {
            ll val = success / spells[i];
            if (success % spells[i]) val++;
            if (val > (ll) INT_MAX) ans[i] = 0;
            else ans[i] = potions.end() - lower_bound(potions.begin(), potions.end(), (int) val);
        }
        return ans;
    }
};