class Union {
    unordered_map<char, char> parent;
public:
    Union() {
        for (char c='a'; c!='z'+1; c++) parent[c] = c;
    }
    
    char find(char c) {
        if (parent[c] != c) parent[c] = find(parent[c]);
        return parent[c];
    }
    
    void link(char c1, char c2) {
        c1 = find(c1);
        c2 = find(c2);
        if (c1 > c2) parent[c1] = c2;
        else parent[c2] = c1;
    }
};

class Solution {
public:
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        Union* U = new Union();
        for (int i=0; i<s1.size(); i++) U->link(s1[i], s2[i]);
        string ans;
        for (char c: baseStr) ans += U->find(c);
        return ans;
    }
};