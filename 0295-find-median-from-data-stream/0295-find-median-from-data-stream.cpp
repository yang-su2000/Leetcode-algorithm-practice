class MedianFinder {
    priority_queue<int> lo; // hi+1 >= lo >= hi
    priority_queue<int, vector<int>, greater<int>> hi;
public:
    MedianFinder() {
    }
    
    void addNum(int num) {
        if (lo.empty() or num < lo.top()) lo.push(num);
        else hi.push(num);
        if (hi.size() > lo.size()) {
            int val = hi.top();
            hi.pop();
            lo.push(val);
        } else if (lo.size() > hi.size() + 1) {
            int val = lo.top();
            lo.pop();
            hi.push(val);
        }
        // if (lo.size() and hi.size()) cout << lo.top() << hi.top() << endl;
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