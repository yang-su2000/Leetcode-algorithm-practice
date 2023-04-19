#define pi pair<int, int>

class Solution {
    vector<vector<pi>> A;
    int N;
    int d;
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        N = n;
        d = distanceThreshold;
        A.resize(n);
        for (auto &v: edges) {
            A[v[0]].push_back({v[2], v[1]});
            A[v[1]].push_back({v[2], v[0]});
        }
        int ans = -1;
        int count = INT_MAX;
        for (int i=0; i<n; i++) {
            int val = dfs(i);
            // cout << i << "->" << val << endl;
            if (val <= count) {
                ans = i;
                count = val;
            }
        }
        return ans;
    }
    
    int dfs(int node) {
        // cout << node << ": ";
        vector<int> dis(N, INT_MAX);
        dis[node] = 0;
        priority_queue<pi, vector<pi>, greater<>> pq;
        pq.push({0, node});
        while (!pq.empty() and pq.top().first <= d) {
            // cout << "[" << pq.top().second << "," << pq.top().first << "]";
            pi cur = pq.top();
            pq.pop();
            for (pi &child: A[cur.second]) {
                int d2 = cur.first + child.first;
                // cout << cur.second << "," << child.second << "," << d2 << " ";
                if (d2 < dis[child.second]) {
                    pq.push({d2, child.second});
                    dis[child.second] = d2;
                }
            }
            // cout << pq.top().first << "..";
        }
        // cout << endl;
        int ret = -1;
        for (int i: dis) {
            // cout << i << " ";
            if (i <= d) ret++;
        }
        // cout << endl;
        return ret;
    }
};