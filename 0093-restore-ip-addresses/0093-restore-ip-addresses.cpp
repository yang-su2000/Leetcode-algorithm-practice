class Solution {
    string S;
public:
    vector<string> restoreIpAddresses(string s) {
        S = s;
        vector<string> ans = rec(0, 4);
        for (string& s: ans) s.pop_back();
        return ans;
    }
    
    vector<string> rec(int i, int dots) {
        // cout << i << " " << dots << endl;
        vector<string> ret;
        if (dots == 0) {
            if (i == S.size()) ret.push_back("");
            return ret;
        }
        if (i + 2 < S.size() and (S[i] == '1' or (S[i] == '2' and (S[i+1] <= '4' or (S[i+1] == '5' and S[i+2] <= '5'))))) {
            string s1 = S.substr(i, 3);
            vector<string> v = rec(i + 3, dots - 1);
            for (auto &s2: v) ret.push_back(s1 + '.' + s2);
        }
        if (i + 1 < S.size() and S[i] != '0') {
            string s1 = S.substr(i, 2);
            vector<string> v = rec(i + 2, dots - 1);
            for (auto &s2: v) ret.push_back(s1 + '.' + s2);
        }
        if (i < S.size()) {
            string s1 = S.substr(i, 1);
            vector<string> v = rec(i + 1, dots - 1);
            for (auto &s2: v) ret.push_back(s1 + '.' + s2);
        }
        return ret;
    }
};