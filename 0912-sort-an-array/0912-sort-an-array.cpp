class Solution {
    vector<int> tmp;
public:
    void quicksort(vector<int>& nums, int l, int r) {
        if (l >= r) return;
        if (l + 1 == r) {
            if (nums[l] > nums[r]) swap(nums[l], nums[r]);
            return;
        }
        int p = l + rand() % (r - l + 1);
        swap(nums[p], nums[r]);
        int pivot = nums[r];
        int l2 = l, r2 = r - 1;
        // cout << l2 << "," << r2 << endl;
        while (l2 <= r2) {
            if (nums[l2] > pivot) swap(nums[l2], nums[r2--]);
            else l2++;
        }
        if (l2 >= 0) swap(nums[r], nums[l2]);
        quicksort(nums, l, l2 - 1);
        quicksort(nums, l2 + 1, r);
    }
    
    void mergesort(vector<int>& nums, int l, int r) {
        if (l == r) return;
        int lr = (l + r) / 2;
        int rl = lr + 1;
        mergesort(nums, l, lr);
        mergesort(nums, rl, r);
        int ll = l;
        int i = l;
        while (i <= r) {
            if (l > lr) tmp[i++] = nums[rl++];
            else if (rl > r) tmp[i++] = nums[l++];
            else if (nums[l] > nums[rl]) tmp[i++] = nums[rl++];
            else tmp[i++] = nums[l++];
        }
        for (i = ll; i <= r; i++) nums[i] = tmp[i];
    }
    
    vector<int> sortArray(vector<int>& nums) {
        int n = nums.size();
        // quicksort(nums, 0, n - 1);
        tmp.resize(n);
        mergesort(nums, 0, n - 1);
        return nums;
    }
};