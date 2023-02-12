#define ll long long

class Solution {
    ll total;
    ll ans = 0;
public:
    ll minimumFuelCost(vector<vector<int>>& roads, ll seats) {
        int n = (int) roads.size() + 1;
        vector<vector<int>> A(n);
        for (auto &r: roads) {
            A[r[0]].emplace_back(r[1]);
            A[r[1]].emplace_back(r[0]);
        }
        total = seats;
        for (int child: A[0]) dfs(A, child, 0);
        return ans;
    }
    
     // return # used seats
     ll dfs(vector<vector<int>>& A, int cur, int parent) {
         ll used_seats = 1;
         for (int child: A[cur]) {
             if (child == parent) continue;
             ll seats = dfs(A, child, cur);
             used_seats += seats;
         }
         ans += used_seats / total;
         if (used_seats % total) ans++;
         return used_seats;
    }
};