class Solution {
public:
    // Dijsktra with all vertex shortest distances
    int networkDelayTime(vector<vector<int>> &times, int n, int k) {
        vector<vector<pair<int, int>>> g(n); // adjcency list
        for (auto &t : times) {
            g[t[0]-1].emplace_back(t[1]-1, t[2]);
        }
        vector<int> dist(n, INT_MAX); // dist[i]: shortest distance from k to i
        dist[k-1] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq; // <dist[i], i>
        pq.emplace(0, k-1);
        while (!pq.empty()) {
            auto p = pq.top(); // shortest dist[i] that <dist[i], i>
            pq.pop();
            for (auto &e : g[p.second]) { // g[i->j] = newd
                int d = p.first + e.second; // previous dist[i] + newd
                if (d < dist[e.first]) { // find shorter
                    dist[e.first] = d; // update dist[j]
                    pq.emplace(d, e.first); // update pq <dist[j], j>
                }
            }
        }
        int ans = *max_element(dist.begin(), dist.end());
        return ans == INT_MAX ? -1 : ans;
    }
};