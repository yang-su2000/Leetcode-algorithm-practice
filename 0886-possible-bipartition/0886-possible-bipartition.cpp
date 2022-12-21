class Union {
public:
    vector<int> p;
    vector<int> r;
    
    Union(int size) {
        for (int i=0; i<size; i++) {
            p.push_back(i);
            r.push_back(-1);
        }
    }
    
    int find(int i) {
        if (p[i] != i) p[i] = find(p[i]);
        return p[i];
    }
    
    void link(int i, int j) {
        i = find(i);
        j = find(j);
        p[j] = p[i];
    }
};

class Solution {
public:
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        Union* U = new Union(n);
        for (int i=0; i<dislikes.size(); i++) {
            int a = dislikes[i][0]-1;
            int b = dislikes[i][1]-1;
            if (U->find(a) == U->find(b)) return false;
            if (U->r[b] != -1) U->link(a, U->r[b]);
            else U->r[b] = a;
            if (U->r[a] != -1) U->link(b, U->r[a]);
            else U->r[a] = b;
        }
        return true;
    }
};