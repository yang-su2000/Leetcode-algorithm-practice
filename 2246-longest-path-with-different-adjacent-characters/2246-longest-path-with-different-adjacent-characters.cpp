class Solution {
    vector<vector<int>> A;
    int n;
    int ans = 0;
public:
    int longestPath(vector<int>& parent, string s) {
        n = parent.size();
        A.resize(n);
        for (int i=1; i<n; i++) A[parent[i]].push_back(i);
        rec(0, s);
        return ans;
    }
    
    // return: max len with node as one end
    int rec(int node, string &s) {
        if (A[node].empty()) {
            ans = max(ans, 1);
            return 1;
        }
        // priority_queue<int, vector<int>, greater<>> pq; // min heap
        char c = s[node];
        int child_ret;
        int max1 = 0, max2 = 0;
        for (int child: A[node]) {
            child_ret = rec(child, s);
            if (s[child] == c) continue;
            if (child_ret > max1) {
                max2 = max1;
                max1 = child_ret;
            } else if (child_ret > max2) {
                max2 = child_ret;
            }
        }
        // for (int child: A[node]) {
        //     child_ret = rec(child, s);
        //     if (s[child] != c) {
        //         pq.push(child_ret);
        //         if (pq.size() > 2) pq.pop();
        //     }
        // }
        // int ret = 1;
        // int ans_ = 1;
        // while (!pq.empty()) {
        //     ret = max(ret, pq.top() + 1);
        //     ans_ += pq.top();
        //     pq.pop();
        // }
        ans = max(ans, max1 + max2 + 1);
        return max(max1, max2) + 1;
    }
};