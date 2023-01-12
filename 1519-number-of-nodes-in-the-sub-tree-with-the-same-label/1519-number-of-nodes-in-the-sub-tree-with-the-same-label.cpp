class Solution {
    vector<int> ans;
    vector<vector<int>> A;
    int N;
public:
    vector<int> countSubTrees(int n, vector<vector<int>>& edges, string labels) {
        ans.resize(n);
        A.resize(n);
        N = n;
        for (vector<int>& e: edges) {
            A[e[0]].push_back(e[1]);
            A[e[1]].push_back(e[0]);
        }
        vector<int> v(26);
        dfs(-1, 0, labels);
        return ans;
    }
    
    vector<int> dfs(int parent, int node, string &s) {
        vector<int> ret(26);
        vector<int> cur;
        for (int child: A[node]) {
            if (child == parent) continue;
            cur = dfs(node, child, s);
            for (int i=0; i<26; i++) ret[i] += cur[i];
        }
        int label = s[node] - 'a';
        ans[node] = ++ret[label];
        return ret;
    }
};