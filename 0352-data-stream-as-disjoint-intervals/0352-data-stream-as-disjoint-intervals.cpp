class SummaryRanges {
    set<pair<int, int>> s;
public:
    SummaryRanges() {
        
    }
    
    void addNum(int val) {
        pair<int, int> p = {val, val};
        if (s.empty()) {
            s.insert(p);
            return;
        }
        auto r = upper_bound(s.begin(), s.end(), p, [](const pair<int, int>& a, const pair<int, int>& b) {return a.first < b.first;});
        if (r == s.end()) { // (a, b) val: a <= val, a <= b
            auto l = prev(r);
            if (l->second + 1 == val) { // (a, val)
                int a = l->first;
                s.erase(l);
                s.insert({a, val});
            } else if (l->second + 1 < val) { // (a, b) (val, val)
                s.insert(p);
            } else {} // (a, val, b)
        } else if (r == s.begin()) { // val (c, d): val < c <= d
            if (val + 1 == r->first) { // (val, d)
                int d = r->second;
                s.erase(r);
                s.insert({val, d});
            } else if (val + 1 < r->first) { // (val, val) (c, d)
                s.insert(p);
            } else {} // impossible
        } else { // (a, b) val (c, d): a <= val, a <= b < c; val < c <= d
            auto l = prev(r);
            if (l->second + 1 == val) {
                if (val + 1 == r->first) { // (a, d)
                    int a = l->first;
                    int d = r->second;
                    s.erase(l);
                    s.erase(r);
                    s.insert({a, d});
                } else { // (a, val) (c, d)
                    int a = l->first;
                    s.erase(l);
                    s.insert({a, val});
                }
            } else if (l->second + 1 < val) {
                if (val + 1 == r->first) { // (a, b) (val, d)
                    int d = r->second;
                    s.erase(r);
                    s.insert({val, d});
                } else { // (a, b) (val, val) (c, d)
                    s.insert(p);
                }
            }
        }
#if 0
        vector<vector<int>> debug = getIntervals();
        for (auto &v: debug) cout << "[" << v[0] << "," << v[1] << "] ";
        cout << endl;
#endif
    }
    
    vector<vector<int>> getIntervals() {
        vector<vector<int>> ans(s.size());
        int i = 0;
        for (auto it=s.begin(); it!=s.end(); it++, i++) ans[i] = {it->first, it->second};
        return ans;
    }
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges* obj = new SummaryRanges();
 * obj->addNum(value);
 * vector<vector<int>> param_2 = obj->getIntervals();
 */