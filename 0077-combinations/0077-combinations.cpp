class Solution {
    vector<vector<int>> ans;
    int N;
    int K;
public:
    void bt(vector<int>& ls) {
        int k_ = ls.size();
        if (k_ == K) {
            ans.push_back(ls);
            return;
        }
        int cur;
        if (ls.empty()) cur = 1;
        else cur = ls.back() + 1;
        if (N - cur + 1 + k_ < K) return;
        for (int i=cur; i<=N; i++) {
            ls.push_back(i);
            bt(ls);
            ls.pop_back();
        }
    }

    vector<vector<int>> combine(int n, int k) {
        N = n;
        K = k;
        vector<int> ls;
        bt(ls);
        return ans;
    }
};