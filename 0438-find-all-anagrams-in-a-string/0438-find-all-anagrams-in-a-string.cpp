class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int ss = s.size();
        int ps = p.size();
        if (ps > ss) return {};
        vector<int> truth(26);
        for (char c: p) truth[c-'a']++;
        vector<int> cur(26);
        for (int i=0; i<ps; i++) cur[s[i]-'a']++;
        vector<int> ans;
        if (cur == truth) ans.push_back(0);
        for (int i=ps; i<ss; i++) {
            cur[s[i-ps]-'a']--;
            cur[s[i]-'a']++;
            if (cur == truth) ans.push_back(i-ps+1);
        }
        return ans;
    }
};