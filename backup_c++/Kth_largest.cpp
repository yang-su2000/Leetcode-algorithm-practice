class Solution {
public:
    int myPartition(vector<int>& a, int l, int r) {
        int pivot = r--;
        while (l < r) {
            if (a[l] <= a[pivot]) l++;
            else swap(a[l], a[r--]);
        }
        swap(a[pivot], a[r+1]);
        int ret = r+1;
        if (a[l] > a[ret]) swap(a[l], a[ret--]);
        return ret;
    }
    
    int findKth_quicksort(vector<int> a, int n, int K) {
        K = n-K;
        int l=0, r=n-1;
        while (l < r-1) {
            int p = myPartition(a, l, r);
            if (p == K) return a[p];
            else if (p > K) r = p-1;
            else l = p+1;
        }
        if (a[l] > a[r]) swap(a[l], a[r]);
        return a[K];
    }
    
    int findKth(vector<int>& a, int n, int K) {
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int &i:a) {
            pq.push(i);
            if (pq.size() > K) pq.pop();
        }
        return pq.top();
    }
};