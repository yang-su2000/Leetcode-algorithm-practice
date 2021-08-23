class Solution {
public:
    int countDigitOne(int n) { // 12345
        long long mult = 1; // 100
        int ans = 0;
        while (n >= mult) { // current 10-bit position: 3
            int rec_before = n / (mult * 10); // count how many rotation before: 12
            int rec = rec_before * mult; // count how many rotation of cur: 1200
            ans += rec;
            int cur = n % (mult * 10); // 345
            if (cur < mult); // 345 < 100, no more digit to add
            else if (cur < 2 * mult) ans += cur - mult + 1; // 100 <= 345 < 200, add 46
            else ans += mult; // 200 <= 345, add 100(maximum digit to add)
            mult *= 10;
        }
        return ans;
    }
};