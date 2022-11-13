class Solution {
public:
    string reverseWords(string s) {
        auto tokens = split(s, " ");
        string ans;
        // for (auto &t:tokens) cout << '[' << t << ']' << endl;
        for (int i = tokens.size()-1; i >= 0; i--) {
            if (!tokens[i].size()) continue;
            ans += tokens[i] + ' ';
        }
        ans.pop_back();
        return ans;
    }
    
    vector<string> split(string s, string regex_s) {
        regex regexz(regex_s);
        return {sregex_token_iterator(s.begin(), s.end(), regexz, -1), \
                sregex_token_iterator()};
    }
};