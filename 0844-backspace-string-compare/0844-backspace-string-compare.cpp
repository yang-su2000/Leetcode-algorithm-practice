class Solution {
public:
    bool backspaceCompare(string S, string T) {
        stack<char> s;
        for (char &c:S) {
            if (c=='#') {
                if (!s.empty()) s.pop();
            } else s.push(c);
        }
        stack<char> t;
        for (char &c:T) {
            if (c=='#') {
                if (!t.empty()) t.pop();
            } else t.push(c);
        }
        /*while (!s.empty() and !t.empty()) {
            if (s.top()==t.top()) {s.pop(); t.pop();}
            else return false;
        }
        return s.empty() and t.empty();*/
        return s==t;
    }
};