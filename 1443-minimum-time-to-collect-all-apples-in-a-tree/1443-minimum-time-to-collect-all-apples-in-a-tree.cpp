class Solution {
    vector<vector<int>> A;
    vector<bool> V;
    int N;
public:
    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        N = n;
        A.resize(n);
        V.resize(n);
        for (vector<int>& e: edges) {
            A[e[0]].push_back(e[1]);
            A[e[1]].push_back(e[0]);
        }
        return rec(0, hasApple);
    }
    
    int rec(int node, vector<bool>& B) {
        V[node] = true;
        int ret = 0;
        int cur;
        for (int &child: A[node]) {
            if (V[child]) continue;
            else cur = rec(child, B);
            if (cur) ret += 2 + cur;
            else if (B[child]) ret += 2;
        }
        // cout << node << " " << ret << endl;
        return ret;
    }
};