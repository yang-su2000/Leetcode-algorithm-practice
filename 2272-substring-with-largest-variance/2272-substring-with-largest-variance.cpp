class Solution {
public:
    int largestVariance(string s) {
        set<char> st;
        for (char c: s) st.insert(c);
        int ans = 0;
        for (char a: st) {
            for (char b: st) {
                if (a == b) continue;
                int val = 0;
                bool a_ = false, b_ = false;
                for (char i: s) {
                    if (i == a) {
                        val++;
                        a_ = true;
                    } else if (i == b) {
                        val--;
                        b_ = true;
                    }
                    if (val < 0) {
                        val = 0;
                        a_ = false;
                        b_ = false;
                    } else if (a_ && b_) {
                        ans = max(ans, val);
                    }
                }
            }
        }
        reverse(s.begin(), s.end());
        for (char a: st) {
            for (char b: st) {
                if (a == b) continue;
                int val = 0;
                bool a_ = false, b_ = false;
                for (char i: s) {
                    if (i == a) {
                        val++;
                        a_ = true;
                    } else if (i == b) {
                        val--;
                        b_ = true;
                    }
                    if (val < 0) {
                        val = 0;
                        a_ = false;
                        b_ = false;
                    } else if (a_ && b_) {
                        ans = max(ans, val);
                    }
                }
            }
        }
        return ans;
    }
};