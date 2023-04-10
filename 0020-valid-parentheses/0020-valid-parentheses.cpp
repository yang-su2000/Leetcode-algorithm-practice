class Solution {
public:
    bool isValid(string s) {
        int n=s.size();
        if (!n) return true;
        stack<char> st; // t1:() t2:[] t3:{}
        char c;
        for (int i=0; i<n; i++){
            c=s[i];
            if (st.size()){
                if ((c==')' and st.top()=='(') or (c==']' and st.top()=='[') or
                    (c=='}' and st.top()=='{')) st.pop();
                else if (c==')' or c== ']' or c=='}') return false;
                else st.push(c);
            } else if (c==')' or c== ']' or c=='}') return false;
            else st.push(c);
        }
        return !st.size();
    }
};