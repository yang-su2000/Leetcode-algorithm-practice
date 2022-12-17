class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        // MUST write both in decreasing order
        // so that |even_idx - odd_idx| has largest dist to avoid median being the same
        // if even: [0, 1, 2, 3]
        // even [1, ., 0, .], range [0, n/2)
        // odd [., 3, ., 2], range [n/2, n)
        // if odd: [0, 1, 2]
        // even first [1, ., 0], range [0, n/2+1)
        // odd last [., 2, .], range [n/2+1, n]
        int n = nums.size();
        vector<int> sorted = nums;
        sort(sorted.begin(), sorted.end());
        int mid = n/2;
        if (n%2) mid++;
        for (int i=mid-1, j=0; i>=0; i--, j+=2) {
            nums[j] = sorted[i];
        }
        for (int i=n-1, j=1; i>=mid; i--, j+=2) {
            nums[j] = sorted[i];
        }
    }
    
    void wiggleSort2(vector<int>& nums) {
        int n = nums.size();
		
		// Step 1: Find the median
        // nth_element(.) is on average O(n)
		auto nth = nums.begin() + n/2;
		nth_element(nums.begin(), nth, nums.end());
		int median = *nth;

		// Step 2: Tripartie partition within O(n)-time & O(1)-space.
        // all elements > median are placed in odd positions
        // all elements < median are placed in even positions
        // all elements == median are placed in the remaining positions
        // where (n | 1) calculates the nearest odd that is not less than n
        
        // suppose original indexes are [0, 1, 2, 3, 4, 5, 6]
        // then median is 3
        // from leftmost, append evens [0, ., 1, ., 2, ., .]
        // from rightmost, append odds [., 6, ., 5, ., 4, .]
        // add median to remaining slot
        // the transformed indexes are [0, 6, 1, 5, 2, 4, 3]
		auto m = [n](int idx) { return (2*idx+1) % (n|1); };
		int first = 0, mid = 0, last = n-1;
		while (mid <= last) {
			if (nums[m(mid)] > median) swap(nums[m(first++)], nums[m(mid++)]);
			else if (nums[m(mid)] < median) swap(nums[m(mid)], nums[m(last--)]);	
			else mid++;
		}
    }
};