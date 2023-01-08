class Solution {
public:
    long long minimumHealth(vector<int>& damage, int armor) {
        long long cur = 1ll;
        int cmax = 0;
        for (int i: damage) {
            cur += i;
            cmax = max(cmax, i);
        }
        return cur - min(armor, cmax);
    }
};