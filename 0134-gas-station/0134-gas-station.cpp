class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        int l = 0, r = 0, g = 0;
        bool loopover = false;
        while (l < n) {
            g += gas[r] - cost[r++];
            if (r == n) {
                loopover = true;
                r = 0;
            }
            if (g < 0) {
                if (loopover) return -1;
                l = r;
                g = 0;
            } else if (l == r) {
                return l;
            }
        }
        return INT_MIN;
    }
};