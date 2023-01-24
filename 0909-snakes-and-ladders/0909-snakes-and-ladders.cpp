class Solution {
public:
    int snakesAndLadders(vector<vector<int>>& board) {
        bool rev = false;
        vector<int> v;
        for (int i=board.size()-1; i>=0; i--) {
            if (rev) reverse(board[i].begin(), board[i].end());
            rev = !rev;
            for (int i: board[i]) v.push_back(i-1); // cout << i-1 << " ";
            // cout << endl;
        }
        int n = v.size();
        vector<set<int>> A(n);
        for (int i=0; i<n; i++) {
            for (int j=i+1; j<=min(i+6, n-1); j++) {
                if (v[j] != -2) A[i].insert(v[j]);
                else A[i].insert(j);
            }
        }
        vector<bool> vis(n);
        vis[0] = true;
        queue<int> q;
        q.push(0);
        int ans = 0;
        while (!q.empty()) {
            ans++;
            int l = q.size();
            while (l--) {
                int i = q.front();
                q.pop();
                for (int j: A[i]) {
                    if (j == n - 1) return ans;
                    if (!vis[j]) {
                        vis[j] = true;
                        q.push(j);
                    }
                }
            }
        }
        return -1;
    }
};