class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> m;
        for (int &i:arr) m[i]++;
        unordered_set<int> s;
        for (auto &[k, v]: m) {
            if (s.count(v)) return false;
            s.insert(v);
        }
        return true;
    }
};