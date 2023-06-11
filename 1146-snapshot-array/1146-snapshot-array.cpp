class SnapshotArray {
    vector<vector<pair<int, int>>> v;
    int snap_id;
public:
    SnapshotArray(int length) {
        v.resize(length);
        snap_id = 0;
    }
    
    void set(int index, int val) {
        if (!v[index].empty() && v[index].back().first == snap_id) {
            v[index].back().second = val;
            return;
        }
        v[index].push_back({snap_id, val});
    }
    
    int snap() {
        return snap_id++;
    }
    
    int get(int index, int snap_id) {
        // for (int i=0; i<v.size(); i++) {
        //     if (v[i].empty()) continue;
        //     cout << i << ": ";
        //     for (auto [id, val]: v[i]) cout << id << ", " << val << "; ";
        //     cout << endl;
        // }
        if (v[index].empty() || v[index][0].first > snap_id) return 0;
        int l = 0, r = v[index].size()-1;
        while (l < r) {
            int mid = l + (r - l) / 2 + 1;
            if (v[index][mid].first > snap_id) r = mid-1;
            else l = mid;
        }
        return v[index][l].second;
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */