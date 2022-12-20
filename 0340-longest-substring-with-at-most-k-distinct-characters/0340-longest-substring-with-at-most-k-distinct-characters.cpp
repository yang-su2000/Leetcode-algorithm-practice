class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        unordered_map<char, int> m;
        int ans = 0;
        int i = 0;
        int j = 0;
        while (j < s.length()) {
            m[s[j]]++;
            while (m.size() > k) {
                if (--m[s[i]] == 0) {
                    m.erase(s[i]);
                }
                i++;
            }
            ans = max(ans, j-i+1);
            j++;
        }
        return ans;
    }
};