#define ll long long

class Solution {
public:
    int maxValue(int n, int index, int maxSum) {
        int l = 0, r = maxSum;
        
        function<bool(int)> solve = [&](ll val) {
            ll csum = val;
            if (index > val - 1) {
                csum += val * (val - 1) / 2;
                csum += index - (val - 1);
            } else {
                csum += ((val - 1) + (val - index)) * index / 2;
            }
            int r = n - index - 1;
            if (r > val - 1) {
                csum += val * (val - 1) / 2;
                csum += r - (val - 1);
            } else {
                csum += ((val - 1) + (val - r)) * r / 2;
            }
            // cout << val << ", " << csum << endl;
            return csum <= maxSum;
        };
        
        while (l < r) {
            int mid = l + (r - l) / 2 + 1;
            if (solve(mid)) l = mid;
            else r = mid - 1;
        }
        return l;
    }
};