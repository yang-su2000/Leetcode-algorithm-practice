class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        int n = tasks.size();
        vector<int> ans;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pt; // processingTime, i
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> et; // enqueueTime, i
        for (int i=0; i<n; i++) et.push({tasks[i][0], i});
        long time = 0;
        while (!et.empty() or !pt.empty()) {
            // no task, move to next task
            if (pt.empty()) {
                time = et.top().first;
                // printf("%d: ", time);
                while (!et.empty() and et.top().first == time) {
                    auto p = et.top();
                    et.pop();
                    // printf("[%d %d]", p.first, p.second);
                    pt.push({tasks[p.second][1], p.second});
                }
                // printf("\n");
            }
            // has task, do it and process time
            auto p = pt.top();
            pt.pop();
            time += p.first;
            ans.push_back(p.second);
            // finish task, load tasks that can be enqueued
            while (!et.empty() and et.top().first <= time) {
                auto p = et.top();
                et.pop();
                pt.push({tasks[p.second][1], p.second});
            }
        }
        return ans;
    }
};