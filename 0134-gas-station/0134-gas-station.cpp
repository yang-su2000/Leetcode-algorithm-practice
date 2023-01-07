class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        int l = 0, r = 0, count = 0, g = 0;
        bool loopover = false;
        while (l < n) {
            g += gas[r] - cost[r];
            r = (r + 1) % n;
            if (r == 0) loopover = true;
            count++;
            if (g < 0) {
                if (loopover) return -1;
                l = r;
                count = 0;
                g = 0;
            } else if (count == n) {
                return l;
            } 
        }
        //     int start = i;
        //     int count = 0;
        //     do {
        //         g += gas[i] - cost[i];
        //         i = (i + 1) % n;
        //         count++;
        //     } while (start != i and g >= 0);
        //     if (start == i and g >= 0) return start;
        //     i = start + count;
        //     g = 0;
        // }
        return -1;
    }
};