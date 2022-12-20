class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<bool> vis(n);
        vis[0] = true;
        stack<int> s;
        s.push(0);
        int count = 1;
        while (!s.empty()) {
            int room = s.top();
            s.pop();
            for (int &room2: rooms[room]) {
                if (vis[room2]) continue;
                vis[room2] = true;
                count++;
                s.push(room2);
            }
        }
        return count == n;
    }
};