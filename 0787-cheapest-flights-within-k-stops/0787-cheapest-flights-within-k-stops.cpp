class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<unordered_map<int, int>> A(n);
        for (auto v: flights) A[v[0]][v[1]] = v[2];
        unordered_map<int, int> d;
        d[src] = 0;
        vector<int> v {src};
        k++;
        while (!v.empty() and k--) {
            unordered_map<int, int> d2;
            vector<int> v2;
            for (int node: v) {
                for (auto [child, dist]: A[node]) {
                    if (d2.count(child)) d2[child] = min(d2[child], dist + d[node]);
                    else d2[child] = dist + d[node];
                }
            }
            for (auto [child, dist]: d2) {
                if (!d.count(child) or dist < d[child]) {
                    v2.emplace_back(child);
                    d[child] = dist;
                }
            }
            v = v2;
        }
        if (d.count(dst)) return d[dst];
        return -1;
    }
};