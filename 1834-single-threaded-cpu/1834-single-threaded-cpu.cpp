#define pii pair<int, int>

class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        int n = tasks.size();
        vector<int> ans;
        priority_queue<pii, vector<pii>, greater<>> pt; // processingTime, i
        priority_queue<pii, vector<pii>, greater<>> et; // enqueueTime, i
        for (int i=0; i<n; i++) et.push({tasks[i][0], i});
        long time = 0;
        while (!et.empty() or !pt.empty()) {
            // no task, move to next task, enqueue all tasks with the same enqueueTime
            if (pt.empty()) {
                time = et.top().first;
                while (!et.empty() and et.top().first == time) {
                    pii p = et.top();
                    et.pop();
                    pt.push({tasks[p.second][1], p.second});
                }
            }
            // has task, do it and add processingTime
            pii p = pt.top();
            pt.pop();
            time += p.first;
            ans.push_back(p.second);
            // finish task, enqueue all tasks that can be enqueued
            while (!et.empty() and et.top().first <= time) {
                pii p = et.top();
                et.pop();
                pt.push({tasks[p.second][1], p.second});
            }
        }
        return ans;
    }
};