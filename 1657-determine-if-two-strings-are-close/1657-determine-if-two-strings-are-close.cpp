class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if (word1.length() != word2.length()) return false;
        vector<int> m1(26), m2(26);
        for (char &c:word1) m1[c-'a']++;
        for (char &c:word2) m2[c-'a']++;
        for (int i=0; i<26; i++) {
            if (m1[i] == 0 and m2[i]) return false;
            if (m2[i] == 0 and m1[i]) return false;
        }
        unordered_map<int, int> m;
        for (int &v: m1) {
            if (!v) continue;
            m[v]++;
        }
        for (int &v: m2) {
            if (!v) continue;
            if (!m.count(v)) return false;
            if (--m[v] == 0) m.erase(v);
        }
        return m.size() == 0;
    }
};