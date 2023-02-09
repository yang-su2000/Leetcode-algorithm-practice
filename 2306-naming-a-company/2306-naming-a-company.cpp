#define ll long long

class Solution {
public:
    long long distinctNames(vector<string>& ideas) {
        vector<unordered_set<string>> css(26); // c to set of string
        for (string &s: ideas) {
            char c = s[0] - 'a';
            string s2 = s.substr(1);
            css[c].insert(s2);
        }
        ll ans = 0;
        for (int i=0; i<25; i++) {
            for (int j=i+1; j<26; j++) {
                int mutual = 0;
                for (string s: css[i]) {
                    if (css[j].count(s)) mutual++;
                }
                ans += 2ll * (css[i].size() - mutual) * (css[j].size() - mutual);
            }
        }
        return ans;
    }
};