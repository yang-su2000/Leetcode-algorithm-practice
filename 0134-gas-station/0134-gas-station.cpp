class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        int i = 0, g = 0;
        while (i < n) {
            int start = i;
            int count = 0;
            do {
                g += gas[i] - cost[i];
                i = (i + 1) % n;
                count++;
            } while (start != i and g >= 0);
            if (start == i and g >= 0) return start;
            i = start + count;
            g = 0;
        }
        return -1;
    }
};