/**
 * // This is the ArrayReader's API interface.
 * // You should not implement it, or speculate about its implementation
 * class ArrayReader {
 *   public:
 *     // Compares the sum of arr[l..r] with the sum of arr[x..y] 
 *     // return 1 if sum(arr[l..r]) > sum(arr[x..y])
 *     // return 0 if sum(arr[l..r]) == sum(arr[x..y])
 *     // return -1 if sum(arr[l..r]) < sum(arr[x..y])
 *     int compareSub(int l, int r, int x, int y);
 *
 *     // Returns the length of the array
 *     int length();
 * };
 */

class Solution {
public:
    int getIndex(ArrayReader &reader) {
        int n = reader.length();
        int l = 0, r = n - 1;
        int mid, range, ret;
        while (l < r) {
            range = r - l;
            if (range % 2) {
                mid = (l + r) / 2;
                ret = reader.compareSub(l, mid, mid + 1, r);
                if (ret == 1) r = mid;
                else if (ret == -1) l = mid + 1;
                else return -1;
            } else {
                mid = (l + r) / 2;
                ret = reader.compareSub(l, mid, mid, r);
                if (ret == 1) r = mid - 1;
                else if (ret == -1) l = mid + 1;
                else return mid;
            }
        }
        return l;
    }
};