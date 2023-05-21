class Solution {
public:
    int shortestBridge(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<pair<int, int>> d = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
        queue<pair<int, int>> cur, vis, vis2;
        bool first = false;
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == 1) {
                    first = true;
                    grid[i][j] = 2;
                    cur.push({i, j});
                    vis.push({i, j});
                    while (!cur.empty()) {
                        auto p = cur.front();
                        cur.pop();
                        for (auto &p2: d) {
                            int i2 = p.first + p2.first;
                            int j2 = p.second + p2.second;
                            if (0 <= i2 && i2 < n && 0 <= j2 && j2 < n \
                                and grid[i2][j2] == 1) {
                                grid[i2][j2] = 2;
                                cur.push({i2, j2});
                                vis.push({i2, j2});
                            }
                        }
                    }
                    break;
                }
            }
            if (first) break;
        }
        int ans = 0;
        while (!vis.empty()) {
            ans++;
            while (!vis.empty()) {
                auto p = vis.front();
                // cout << p.first << " " << p.second << " " << ans << endl;
                vis.pop();
                for (auto &p2: d) {
                    int i2 = p.first + p2.first;
                    int j2 = p.second + p2.second;
                    if (0 <= i2 && i2 < n && 0 <= j2 && j2 < n) {
                        if (grid[i2][j2] == 1) return ans - 1;
                        if (grid[i2][j2] == 0) {
                            grid[i2][j2] = 2;
                            vis2.push({i2, j2});
                        }
                    }
                }
            }
            swap(vis, vis2);
        }
        return -1;
    }
};