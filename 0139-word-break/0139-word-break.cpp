class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.length();
        int m = wordDict.size();
        vector<bool> b(n + 1);
        b[0] = true;
        for (int i=1; i<=n; i++) {
            for (string &word: wordDict) {
                int l = word.length();
                if (i >= l && b[i-l] && s.substr(i-l, l) == word) {
                    b[i] = true;
                    break;
                }
            }
        }
        return b[n];
    }
};