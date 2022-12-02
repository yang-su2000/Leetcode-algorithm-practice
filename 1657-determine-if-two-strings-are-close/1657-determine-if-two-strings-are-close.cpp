class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if (word1.length() != word2.length()) return false;
        unordered_map<char, int> m1, m2;
        for (char &c:word1) m1[c]++;
        for (char &c:word2) m2[c]++;
        set<char> keys;
        multiset<int> vals;
        for (auto &[k, v]: m1) {
            keys.insert(k);
            vals.insert(v);
        }
        for (auto &[k, v]: m2) {
            if (!keys.count(k)) return false;
            keys.erase(k);
            if (!vals.count(v)) return false;
            vals.erase(vals.find(v));
        }
        return keys.size() == 0 and vals.size() == 0;
    }
};