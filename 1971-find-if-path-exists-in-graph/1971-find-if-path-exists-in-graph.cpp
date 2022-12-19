class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        vector<vector<int>> v(n);
        for (auto &e:edges) {
            v[e[0]].push_back(e[1]);
            v[e[1]].push_back(e[0]);
        }
        if (source == destination) return true;
        if (v[source].empty()) return false;
        vector<bool> vis(n);
        stack<int> s;
        vis[source] = true;
        s.push(source);
        while (!s.empty()) {
            int cur = s.top();
            s.pop();
            for (int &nxt: v[cur]) {
                if (!vis[nxt]) {
                    if (nxt == destination) return true;
                    vis[nxt] = true;
                    s.push(nxt);
                }
            }
        }
        return false;
    }
};