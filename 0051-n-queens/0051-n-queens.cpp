class Solution {
    vector<vector<string>> ans;
    int N;
    int dead_end;
public:
    vector<vector<string>> solveNQueens(int n) {
        N = n;
        dead_end = (1 << N) - 1;
        vector<int> cur;
        backtrack(cur);
        return ans;
    }
    
    void backtrack(vector<int>& cur) {
        // for (int i: cur) cout << i << " ";
        // cout << endl;
        int len = cur.size();
        if (len == N) {
            vector<string> ans_;
            for (int i: cur) {
                string s = string(i, '.') + 'Q' + string(N - i - 1, '.');
                ans_.push_back(s);
            }
            ans.push_back(ans_);
            return;
        }
        int taken = 0;
        int val;
        int diff;
        for (int i=0; i<len; i++) {
            val = cur[i];
            taken |= (1 << val);
            diff = len - i;
            if (val - diff >= 0) taken |= (1 << (val - diff));
            if (val + diff < N) taken |= (1 << (val + diff));
        }
        // cout << bitset<10>(taken) << " #" << endl;
        if (taken == dead_end) return;
        for (int i=0; i<N; i++) {
            if (taken & (1 << i)) continue;
            cur.push_back(i);
            backtrack(cur);
            cur.pop_back();
        }
    }
};