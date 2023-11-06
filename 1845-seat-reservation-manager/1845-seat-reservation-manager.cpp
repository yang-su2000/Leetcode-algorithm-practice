class SeatManager {
    set<int> re, unre;
public:
    SeatManager(int n) {
        for (int i=1; i<=n; i++) unre.insert(i);
    }
    
    int reserve() {
        int seat = *unre.begin();
        unre.erase(unre.begin());
        re.insert(seat);
        return seat;
    }
    
    void unreserve(int seat) {
        re.erase(seat);
        unre.insert(seat);
    }
};

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager* obj = new SeatManager(n);
 * int param_1 = obj->reserve();
 * obj->unreserve(seatNumber);
 */