class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> m;
        for (char &c:s) m[c]++;
        multimap<int, char> m2;
        for (auto &[k, v]: m) m2.insert({v, k});
        string ans;
        for (auto &[k, v]: m2) {
            for (int i=0; i<k; i++) ans += v;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};