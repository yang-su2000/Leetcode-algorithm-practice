class Solution {
public:
    string makeGood(string s) {
        string ans;
        for (char &c:s) {
            if (ans.length() and (abs(c - ans.back()) == 32)) {
                ans.pop_back();
            } else ans.push_back(c);
        }
        return ans;
    }
};