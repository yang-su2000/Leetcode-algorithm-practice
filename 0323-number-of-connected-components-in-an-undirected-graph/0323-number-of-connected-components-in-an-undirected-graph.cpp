class Union {
    vector<int> p;
public:
    Union(int size) {
        p.resize(size);
        for (int i=0; i<size; i++) p[i] = i;
    }
    
    int find(int i) {
        if (p[i] != i) p[i] = find(p[i]);
        return p[i];
    }
    
    void link(int i, int j) {
        i = find(i);
        j = find(j);
        p[i] = p[j];
    }
};

class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        Union* U = new Union(n);
        for (auto &v:edges) {
            U->link(v[0], v[1]);
        }
        set<int> s;
        for (int i=0; i<n; i++) s.insert(U->find(i));
        return s.size();
    }
};