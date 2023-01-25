class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        stack<int> s;
        for (int i: arr) {
            if (s.empty() or i >= s.top()) s.push(i);
            else {
                int hi = s.top();
                while (!s.empty() and i < s.top()) s.pop();
                s.push(hi);
            }
        }
        return (int) s.size();
    }
};