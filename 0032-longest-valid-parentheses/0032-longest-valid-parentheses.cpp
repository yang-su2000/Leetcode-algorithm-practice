class Solution {
public:
    int longestValidParentheses(string s) {
        int ans = 0;
        vector<int> st; // 0: (, ow: len
        for (char &c: s) {
            if (c == '(') {
                st.push_back(0);
            } else if (!st.empty()) {
                int t = st.back();
                if (t == 0) {
                    st.pop_back();
                    int len = 2;
                    while (!st.empty() and st.back()) {
                        len += st.back();
                        st.pop_back();
                    }
                    st.push_back(len);
                    ans = max(ans, len);
                } else {
                    int len = st.back();
                    st.pop_back();
                    if (!st.empty() and st.back() == 0) {
                        len += 2;
                        st.pop_back();
                        while (!st.empty() and st.back()) {
                            len += st.back();
                            st.pop_back();
                        }
                        st.push_back(len);
                        ans = max(ans, len);
                    } else {
                        while (!st.empty()) st.pop_back();
                    }
                }
            }
            // cout << c << ":";
            // for (int &i: st) cout << i << " ";
            // cout << endl;
        }
        return ans;
    }
};