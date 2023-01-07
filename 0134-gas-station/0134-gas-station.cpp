class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        int l = 0, r = 0;
        int g = 0;
        while (l < n) {
            do {
                g += gas[r] - cost[r];
                r = (r + 1) % n;
            } while (l != r and g >= 0);
            if (l == r and g >= 0) return l;
            while (l < n and g < 0) {
                g += cost[l] - gas[l];
                l++;
            }
        }
        return -1;
    }
};