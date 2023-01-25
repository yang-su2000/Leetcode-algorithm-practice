class Solution {
public:
    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        int n = edges.size();
        vector<int> v1(n, -1), v2(n, -1);
        v1[node1] = 0;
        v2[node2] = 0;
        while (1) {
            int child = edges[node1];
            if (child != -1 and v1[child] == -1) {
                v1[child] = v1[node1] + 1;
                node1 = child;
            } else {
                break;
            }
        }
        while (1) {
            int child = edges[node2];
            if (child != -1 and v2[child] == -1) {
                v2[child] = v2[node2] + 1;
                node2 = child;
            } else {
                break;
            }
        }
        // for (int i: v1) cout << i << " ";
        // cout << endl;
        // for (int i: v2) cout << i << " ";
        // cout << endl;
        int d = INT_MAX;
        int ans = -1;
        for (int i=0; i<n; i++) {
            if (v1[i] == -1 or v2[i] == -1) continue;
            int d_ = max(v1[i], v2[i]);
            if (d_ < d) {
                d = d_;
                ans = i;
            } else if (d_ == d and i < ans) ans = i;
        }
        return ans;
    }
};