class MyStack {
    queue<int> q1, q2;
public:
    MyStack() {
        
    }
    
    void push(int x) {
        q1.push(x);
    }
    
    int pop() {
        while (q1.size() > 1) {
            int v = q1.front();
            q1.pop();
            q2.push(v);
        }
        int v = q1.front();
        q1.pop();
        swap(q1, q2);
        return v;
    }
    
    int top() {
        while (q1.size() > 1) {
            int v = q1.front();
            q1.pop();
            q2.push(v);
        }
        int v = q1.front();
        q1.pop();
        q2.push(v);
        swap(q1, q2);
        return v;
    }
    
    bool empty() {
        return q1.empty() && q2.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */