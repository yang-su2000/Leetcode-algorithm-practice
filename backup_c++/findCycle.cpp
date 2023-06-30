class Solution {
public:
    int safe(vector<vector<int>>& g, vector<int>& color, int x) {
        if (color[x] > 0) {
            return color[x] == 2;
        }
        color[x] = 1;
        for (int y : g[x]) {
            if (!safe(g, color, y)) {
                return false;
            }
        }
        color[x] = 2;
        return true;
    }

    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n=graph.size();
        vector<int> color(n);
        vector<int> ans;
        for (int i=0; i<n; i++) {
            if (safe(graph, color, i)) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};