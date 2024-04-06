class Solution {
public:
    string minRemoveToMakeValid(string s) {
        stack<int> idx;
        for (int i=0; i<s.size(); i++) {
            if (s[i]=='(') idx.push(i);
            else if (s[i]==')') {
                if (idx.empty()) {
                    s.erase(s.begin()+i);
                    i--;
                } else idx.pop();
            } else continue;
        }
        while (!idx.empty()) {
            s.erase(s.begin()+idx.top());
            idx.pop();
        }
        return s;
    }
};