class Solution {
public:
    string minWindow(string s1, string s2) {
        int n = s1.length();
        int l = n;
        int le = n + 1;
        for (int l2=0; l2<n; l2++) {
            int r = l2;
            bool valid = true;
            for (char c: s2) {
                while (r < n and s1[r] != c) r++;
                if (r == n) {
                    valid = false;
                    break;
                }
                r++;
            }   
            r--;
            if (!valid) continue;
            int le2 = r - l2 + 1;
            if (le2 < le) {
                le = le2;
                l = l2;
            }
        }
        if (l == n) return "";
        return s1.substr(l, le);
    }
};