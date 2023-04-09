class Solution {
    vector<vector<int>> A;
    vector<vector<int>> feat;
    vector<int> mark;
    string color;
    int n;
    int m;
    int ans = 0;
public:
    int largestPathValue(string colors, vector<vector<int>>& edges) {
        color = colors;
        n = colors.length();
        m = edges.size();
        A.resize(n);
        for (auto &p: edges) {
            A[p[0]].push_back(p[1]);
        }
        feat.resize(n, vector<int>(26));
        mark.resize(n); // 0 not, 1 cur, 2 done
        for (int i=0; i<n; i++) {
            visit(i);
        }
        // debug
        // for (int i=0; i<n; i++) {
        //     for (int i: feat[i]) cout << i;
        //     cout << endl;
        // }
        return ans;
    }
    
    void visit(int node) {
        if (ans == -1 or mark[node] == 2) return;
        if (mark[node] == 1) {
            ans = -1;
            return;
        }
        mark[node] = 1;
        
        for (int child: A[node]) {
            visit(child);
            if (ans == -1) return;
            for (int c=0; c<26; c++) {
                feat[node][c] = max(feat[node][c], feat[child][c]);
            }
        }
        feat[node][color[node]-'a']++;
        for (int c=0; c<26; c++) ans = max(ans, feat[node][c]);
        mark[node] = 2;
    }
};