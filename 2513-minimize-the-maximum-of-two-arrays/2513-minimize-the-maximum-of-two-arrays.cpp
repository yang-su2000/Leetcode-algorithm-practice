class Solution {
    long long lcm;
    // int g;
public:
    int minimizeSet(int divisor1, int divisor2, int uniqueCnt1, int uniqueCnt2) {
        lcm = ((long long) divisor1 * divisor2) / gcd(divisor1, divisor2);
        // g = gcd(divisor1, divisor2);
        int l = 0, r = INT_MAX;
        while (l < r) {
            int mid = (r - l) / 2 + l;
            bool flag = isValid(divisor1, divisor2, uniqueCnt1, uniqueCnt2, mid);
            // cout << " " << flag << endl;
            if (flag) r = mid;
            else l = mid+1;
        }
        return r;
    }
    
    
    bool isValid(int d1, int d2, int c1, int c2, int x) {
        int nd1 = x - x / d1;
        int nd2 = x - x / d2;
        long long nd = (long long) x - x / d1 - x / d2 + x / lcm;
        // cout << x << " " << nd1 << " " << nd2 << " " << nd;
        if (nd1 < c1) return false;
        if (nd2 < c2) return false;
        if (x < c1 + c2) return false;
        if ((long long) nd1 + nd2 < c1 + c2 + nd) return false;
        // if (nd1 - nd < c1 and nd2 - nd < c2) return false;
        return true;
    }
};