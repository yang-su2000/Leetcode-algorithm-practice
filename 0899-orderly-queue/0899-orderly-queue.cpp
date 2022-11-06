class Solution {
public:
    string orderlyQueue(string s, int k) {
        if (k == 1) {
            string ans = s;
            for (int i=0; i<s.length(); i++) {
                s = s.substr(1) + s[0];
                ans = min(ans, s);
            }
            return move(ans);
        } else {
            sort(s.begin(), s.end());
            return move(s);
        }
    }
};