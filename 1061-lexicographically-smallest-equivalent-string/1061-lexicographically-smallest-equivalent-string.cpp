class Union {
    vector<int> parent;
public:
    Union() {
        parent.resize(26);
        for (int c=0; c<26; c++) parent[c] = c;
    }
    
    int find(int c) {
        if (parent[c] != c) parent[c] = find(parent[c]);
        return parent[c];
    }
    
    void link(int c1, int c2) {
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
        for (int i=0; i<s1.size(); i++) U->link(s1[i]-'a', s2[i]-'a');
        string ans;
        for (char c: baseStr) ans += U->find(c-'a') + 'a';
        return ans;
    }
};