class Solution {
public:
    int longestSubstring(string s, int k) {
        int n = s.size();
        if (k == 1) return n;
        if (n == 1) return 0;
        unordered_map<int, int> idx;
        vector<vector<int>> psum(n, vector<int>(26));
        psum[0][s[0]-'a']++;
        idx[s[0]-'a'] = 0;
        int ans = 0;
        for (int i=1; i<n; i++) {
            idx[s[i]-'a'] = i;
            bool valid = true;
            for (int c=0; c<26; c++) {
                if (s[i]-'a' == c) psum[i][c] = psum[i-1][c]+1;
                else psum[i][c] = psum[i-1][c];
                if (0 < psum[i][c] and psum[i][c] < k) valid = false;
            }
            if (valid) ans = max(ans, i+1);
            bool valid2;
            int count;
            for (auto [c, l]: idx) {
                valid2 = true;
                for (auto [c2, l2]: idx) {
                    count = psum[i][c2] - psum[l][c2];
                    if (0 < count and count < k) {valid2 = false; break;}
                }
                if (valid2) ans = max(ans, i-l);
            }
        }
        return ans;
    }
    
    // int longestSubstring(string s, int k) {
    //     s += ' ';
    //     vector<pair<char, int>> v;
    //     char c = s[0];
    //     int count = 1;
    //     for (int i=1; i<s.size(); i++) {
    //         if (s[i] == c) count++;
    //         else {
    //             v.push_back({c, count});
    //             printf("%c %d\n", c, count);
    //             c = s[i];
    //             count = 1;
    //         }
    //     }
    //     return foo(v, k);
    // }
};