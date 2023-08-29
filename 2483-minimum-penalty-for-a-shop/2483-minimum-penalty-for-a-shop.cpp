class Solution {
public:
    int bestClosingTime(string s) {
        int n = s.length();
        int y1 = 0, n1 = 0;
        int y2 = 0, n2 = 0;
        for (char c: s) {
            if (c == 'Y') y2++;
            else n2++;
        }
        int ans = 0;
        int p = n1 + y2;
        for (int i=0; i<n; i++) {
            if (s[i] == 'Y') {
                y1++;
                y2--;
            } else {
                n1++;
                n2--;
            }
            if (n1 + y2 < p) {
                p = n1 + y2;
                ans = i + 1;
            }
        }
        return ans;
    }
};