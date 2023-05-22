class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> win;
        for (int &i:nums) win[i]++;
        priority_queue<pair<int, int>,vector<pair<int,int>>, greater<pair<int,int>>> pq;
        for (auto &p:win) {
            if (pq.size()==k) {
                if (pq.top().first<p.second){
                    pq.pop();
                    pq.push({p.second,p.first});
                }
            } else pq.push({p.second,p.first});
        }
        vector<int> ans;
        int i=0;
        while (i<k) {
            ans.push_back(pq.top().second);
            pq.pop();
            i++;
        }
        return ans;
    }
};