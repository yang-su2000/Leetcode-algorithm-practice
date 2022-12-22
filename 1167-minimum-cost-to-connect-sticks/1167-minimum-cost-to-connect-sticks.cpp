class Solution {
public:
    int connectSticks(vector<int>& sticks) {
        int ans = 0;
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int &i: sticks) pq.push(i);
        while (pq.size() > 1) {
            int i = pq.top();
            pq.pop();
            int j = pq.top();
            pq.pop();
            ans += i + j;
            pq.push(i + j);
        }
        return ans;
    }
};