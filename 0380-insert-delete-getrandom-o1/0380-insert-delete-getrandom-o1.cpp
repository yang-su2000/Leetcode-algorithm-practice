class RandomizedSet {
    unordered_map<int, int> m;
    vector<int> v;
public:
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        if (!m.count(val)) {
            m[val] = v.size();
            v.emplace_back(val);
            return true;
        }
        return false;
    }
    
    bool remove(int val) {
        if (m.count(val)) {
            int i = m[val];
            int back = v.back();
            v[i] = back;
            m[back] = i;
            m.erase(val);
            v.pop_back();
            return true;
        }
        return false;
    }
    
    int getRandom() {
        return v[rand() % v.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */