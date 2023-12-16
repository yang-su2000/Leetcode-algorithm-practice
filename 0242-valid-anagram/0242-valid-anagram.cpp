class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> smap(127);
        vector<int> tmap(127);
        for (char c: s) smap[c]++;
        for (char c: t) tmap[c]++;
        return smap == tmap;
    }
};