class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        int l = 0, r = 0;
        int g = 0;
        while (l < n) {
            bool moved = false;
            while (l != r or !moved) {
                moved = true;
                g += gas[r] - cost[r];
                r = (r + 1) % n;
                // cout << "[" << r << " " << g << "] ";
                if (g < 0) break;
            }
            // cout << l << " " << r << " " << g << ", ";
            if (l == r and g >= 0) return l;
            while (l < n and g < 0) {
                g += cost[l] - gas[l];
                l++;
            }
            // cout << l << " " << r << " " << g << endl;
        }
        return -1;
    }
};