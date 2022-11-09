class StockSpanner {
    int i = 0;
    vector<int> lo_stack;
    vector<int> idxs;
public:
    StockSpanner() {
        
    }
    
    int next(int price) {
        int cur = i;
        int idx = i;
        while (!lo_stack.empty() and lo_stack.back() <= price) {
            lo_stack.pop_back();
            idx = idxs.back();
            idxs.pop_back();
        }
        lo_stack.push_back(price);
        idxs.push_back(idx);
        i++;
        return cur-idx+1;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */