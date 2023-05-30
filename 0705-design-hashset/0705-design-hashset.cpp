class MyHashSet {
    vector<bool> ht;
public:
    /** Initialize your data structure here. */
    MyHashSet() {
        ht.resize(1e6+1);
    }
    
    void add(int key) {
        ht[key]=true;
    }
    
    void remove(int key) {
        ht[key]=false;
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        return ht[key];
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */