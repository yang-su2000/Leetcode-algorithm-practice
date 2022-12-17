class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<long> st;
        int i;
        for (string &s:tokens) {
            if (s == "+") {
                i = st.top();
                st.pop();
                st.top() += i;
            } else if (s == "-") {
                i = st.top();
                st.pop();
                st.top() -= i;
            } else if (s == "*") {
                i = st.top();
                st.pop();
                st.top() *= i;
            } else if (s == "/") {
                i = st.top();
                st.pop();
                st.top() /= i;
            } else {
                st.push(stoi(s));
            }
        }
        return st.top();
    }
};