class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        unordered_map<int, int> m; // 0 all win, 1 one lose, 2 more loses
        for (auto &v: matches) {
            int win = v[0];
            int lose = v[1];
            if (!m.count(win)) m[win] = 0;
            if (!m.count(lose)) m[lose] = 1;
            else {
                int status = m[lose];
                if (status == 0) m[lose] = 1;
                else if (status == 1) m[lose] = 2;
            }
        }
        set<int> ans0;
        set<int> ans1;
        for (auto &[k, v]: m) {
            if (v == 0) ans0.insert(k);
            else if (v == 1) ans1.insert(k);
        }
        vector<int> v0 (ans0.begin(), ans0.end());
        vector<int> v1 (ans1.begin(), ans1.end());
        return {v0, v1};
    }
};