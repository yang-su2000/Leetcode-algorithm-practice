/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

class NestedIterator {
    vector<int> v;
    int i=0;
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        for (auto &ni: nestedList) trace(ni);
    }
    
    void trace(NestedInteger &ni) {
        if (ni.isInteger()) v.push_back(ni.getInteger());
        else for (auto &ni2: ni.getList()) trace(ni2);
    }
    
    int next() {
        return v[i++];
    }
    
    bool hasNext() {
        return i < v.size();
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */