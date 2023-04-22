class Solution {
public:
    bool isSubsequence(string s, string t) {
        int si = 0, ti = 0;
        while (si < s.length() and ti < t.length()) {
            if (s[si] == t[ti++]) si++;
        }
        return (si == s.length());
    }
};