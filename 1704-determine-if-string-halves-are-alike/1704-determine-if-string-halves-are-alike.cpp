class Solution {
public:
    bool halvesAreAlike(string s) {
        unordered_set<char> st {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        int a = 0;
        int b = 0;
        for (int i=0; i<s.length()/2; i++) {
            if (st.count(s[i])) a++;
        }
        for (int i=s.length()/2; i<s.length(); i++) {
            if (st.count(s[i])) b++;
        }
        return a == b;
    }
};