class Union {
    vector<int> parent;
public:
    Union(int n) {
        parent.resize(n);
        for (int i=0; i<n; i++) parent[i] = i;
    }
    
    int find(int i) {
        if (parent[i] != i) {
            parent[i] = find(parent[i]);
            return parent[i];
        }
        return i;
    }
    
    void link(int i, int head) {
        i = find(i);
        head = find(head);
        parent[i] = head;
    }
};

class Solution {
public:
    int numberOfGoodPaths(vector<int>& vals, vector<vector<int>>& edges) {
        int n = vals.size();
        vector<vector<int>> A(n);
        for (vector<int>& e: edges) {
            A[e[0]].push_back(e[1]);
            A[e[1]].push_back(e[0]);
        }
        map<int, vector<int>> m;
        for (int i=0; i<n; i++) m[vals[i]].push_back(i);
        Union U(n);
        int ans = 0;
        for (auto &[value, v]: m) {
            for (int node: v) {
                for (int child: A[node]) {
                    if (vals[child] > value) continue;
                    U.link(child, node);
                }
            }
            unordered_map<int, int> m_count;
            for (int node: v) m_count[U.find(node)]++;
            for (auto &[_, count]: m_count) ans += (count + 1) * count / 2;
        }
        return ans;
    }
};