class MyHashSet {
    vector<vector<bool>> ht;
    int mod;
    int d;
    int r;
public:
    /** Initialize your data structure here. */
    MyHashSet() {
        mod = 1e3;
    }
    
    void resize(int key) {
        d = key / mod;
        r = key % mod;
        if (ht.size() <= d) ht.resize(d+1);
        if (ht[d].size() <= r) ht[d].resize(r+1);
    }
    
    void add(int key) {
        resize(key);
        ht[d][r] = true;
    }
    
    void remove(int key) {
        resize(key);
        ht[d][r] = false;
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        resize(key);
        return ht[d][r];
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */