class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& pres) {
        vector<int> pre_count(numCourses);
        vector<stack<int>> childs(numCourses);
        for (auto &v: pres) {
            childs[v[1]].push(v[0]);
            pre_count[v[0]]++;
        }
        stack<int> s;
        int finished = 0;
        for (int i=0; i<numCourses; i++) {
            if (pre_count[i] == 0) s.push(i);
        }
        while (!s.empty()) {
            int course = s.top();
            s.pop();
            finished++;
            stack<int> &s2 = childs[course];
            while (!s2.empty()) {
                int next_course = s2.top();
                s2.pop();
                if (--pre_count[next_course] == 0) s.push(next_course);
            }
        }
        return finished == numCourses;
    }
};