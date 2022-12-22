class Solution {
public:
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        vector<int> childs(n);
        vector<vector<int>> A(n);
        for (auto &e:edges) {
            A[e[0]].push_back(e[1]);
            A[e[1]].push_back(e[0]);
        }
        // begin dfs
        stack<pair<int, int>> s; // val, level
        vector<bool> vis(n);
        int hc = 0;
        s.push({0, 0});
        while (!s.empty()) {
            int node = s.top().first;
            int level = s.top().second;
            if (vis[node]) {
                s.pop();
                int count = 1;
                for (int child: A[node]) {
                    if (!vis[child]) continue;
                    count += childs[child];
                }
                childs[node] = count;
            } else {
                vis[node] = true;
                hc += level;
                for (int child: A[node]) {
                    if (vis[child]) continue;
                    s.push({child, level + 1});
                }
            }
        }
        // for (int i: childs) printf("%d ", i);
        // printf("\nhc = %d\n", hc);
        // end dfs
        // begin dfs2
        stack<int> s2;
        vector<int> ans(n);
        vector<bool> vis2(n);
        s2.push(0);
        ans[0] = hc;
        vis2[0] = true;
        while (!s2.empty()) {
            int node = s2.top();
            s2.pop();
            for (int child: A[node]) {
                if (vis2[child]) continue;
                vis2[child] = true;
                s2.push(child);
                ans[child] = ans[node] + n - 2 * childs[child];
            }
        }
        // end dfs2
        return ans;
    }
};