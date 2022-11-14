class Union {
    vector<int> parent;
public:
    Union(int n) {
        parent.resize(n);
        for (int i=0; i<n; i++) parent[i]=i;
    }
    int find(int i) {
        if (parent[i]!=i) parent[i]=find(parent[i]);
        return parent[i];
    }
    void link(int a, int b) {
        parent[find(a)]=find(b);
    }
};

class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        Union U(20001);
        int n=stones.size();
        for (int i=0; i<n; i++) U.link(stones[i][0], stones[i][1]+10000);
        set<int> seen;
        for (int i=0; i<n; i++) seen.insert(U.find(stones[i][0]));
        return n-seen.size();
    }
};