class SnapshotArray {
    vector<vector<pair<int, int>>> v;
    int snap_id;
public:
    SnapshotArray(int length) {
        v.resize(length);
        for (int i=0; i<length; i++) v[i].push_back(make_pair(0, 0));
        snap_id = 0;
    }
    
    void set(int index, int val) {
        v[index].push_back(make_pair(snap_id, val));
    }
    
    int snap() {
        return snap_id++;
    }
    
    int get(int index, int snap_id) {
        auto it = upper_bound(v[index].begin(), v[index].end(), make_pair(snap_id, INT_MAX));
        return prev(it)->second;
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */