class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int m = strs[0].size();
        int ans = 0;
        for (int i=0; i<m; i++) {
            char c = 'a' - 1;
            for (auto &s: strs) {
                if (s[i] < c) {
                    ans++;
                    break;
                } else c = s[i];
            }
        }
        return ans;
    }
};