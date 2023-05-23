class KthLargest {
    priority_queue<int, vector<int>, greater<int>> pq;
    int cap;
public:
    KthLargest(int k, vector<int>& nums) {
        cap = k;
        for (int i: nums) {
            pq.push(i);
            if (pq.size() > cap) pq.pop();
        }
    }
    
    int add(int val) {
        pq.push(val);
        // cout << pq.top();
        if (pq.size() > cap) pq.pop();
        // cout << " " << pq.top() << endl;
        return pq.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */