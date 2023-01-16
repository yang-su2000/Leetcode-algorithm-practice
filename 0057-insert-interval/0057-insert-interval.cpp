class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        int start=newInterval[0], end=newInterval[1];
        int i=0, n=intervals.size();
        vector<vector<int>> ans;
        while (i<n and start>intervals[i][0]) ans.push_back(intervals[i++]);
        vector<int> cur(2);
        if (ans.empty() or ans.back()[1]<start) ans.push_back(newInterval);
        else ans.back()[1]=max(ans.back()[1],end);
        while (i<n){
            cur=intervals[i++];
            if (ans.back()[1]<cur[0]) ans.push_back(cur);
            else ans.back()[1]=max(ans.back()[1],cur[1]);
        }
        return ans;
    }
};