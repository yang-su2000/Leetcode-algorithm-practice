class Solution {
public:
    string removeDuplicates(string s) {
        string ans;
        for (char &c:s) {
            ans.push_back(c);
            while (ans.length() >= 2 and *ans.rbegin() == *(ans.rbegin()+1)) {
                ans.pop_back();
                ans.pop_back();
            }
        }
        return ans;
    }
};