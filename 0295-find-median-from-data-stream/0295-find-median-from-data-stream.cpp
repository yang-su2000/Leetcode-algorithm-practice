class MedianFinder {
    priority_queue<int> lo; // hi+1 >= lo >= hi
    priority_queue<int, vector<int>, greater<int>> hi;
public:
    MedianFinder() {
    }
    
    void addNum(int num) {
        lo.push(num);
        hi.push(lo.top());
        lo.pop();
        if (hi.size() > lo.size()) {
            lo.push(hi.top());
            hi.pop();
        }
    }
    
    double findMedian() {
        if (lo.size() > hi.size()) return lo.top();
        else return (double) (lo.top() + hi.top()) / 2;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */