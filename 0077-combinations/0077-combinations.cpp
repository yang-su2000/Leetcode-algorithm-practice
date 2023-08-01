class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ans;
        function<void(vector<int>&)> bt = [&](vector<int>& ls) {
            int k_ = ls.size();
            if (k_ == k) {
                ans.push_back(ls);
                return;
            }
            int cur;
            if (ls.empty()) cur = 1;
            else cur = ls.back() + 1;
            if (n - cur + 1 + k_ < k) return;
            for (int i=cur; i<=n; i++) {
                ls.push_back(i);
                bt(ls);
                ls.pop_back();
            }
        };
        vector<int> tmp;
        bt(tmp);
        return ans;
    }
};