class SeatManager {
    priority_queue<int, vector<int>, greater<>> unre;
public:
    SeatManager(int n) {
        for (int i=1; i<=n; i++) unre.push(i);
    }
    
    int reserve() {
        int seat = unre.top();
        while (!unre.empty() && unre.top() == seat) unre.pop();
        return seat;
    }
    
    void unreserve(int seat) {
        unre.push(seat);
    }
};

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager* obj = new SeatManager(n);
 * int param_1 = obj->reserve();
 * obj->unreserve(seatNumber);
 */