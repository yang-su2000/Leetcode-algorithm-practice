class Solution {
public:
    string reverseWords(string s) {
        s += ' ';
        vector<string> ls;
        int i=0;
        string cur;
        for (char &c:s) {
            if (c == ' ') {
                if (cur.size()) {
                    ls.push_back(cur);
                    cur.clear();
                }
            } else cur += c;
        }
        string ans;
        for (int i=ls.size()-1; i>=0; i--) ans += ls[i] + ' ';
        ans.pop_back();
        return ans;
    }
};